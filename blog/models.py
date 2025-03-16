from typing import Tuple

from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from blog.utils.slug_from_title import generate_slug_from_title
from common.models import BaseModel

User = get_user_model()


class Article(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, max_length=200)
    content = models.TextField(verbose_name=_('Content'), )
    topic = models.ForeignKey('blog.Topic', verbose_name=_('Topic'), related_name='articles',
                              on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('blog.Tag', verbose_name=_('Tags'), related_name='articles', blank=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='blog/article_images/', blank=True, null=True)
    is_published = models.BooleanField(_('Is published'), default=True)
    series = models.ForeignKey('ArticleSeries', verbose_name=_('Series'), related_name='articles',
                               on_delete=models.SET_NULL, null=True, blank=True)
    series_sequence_number = models.PositiveIntegerField(verbose_name=_('Series sequence number'), null=True,
                                                         blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.series and self.series_sequence_number is None:
            self.series_sequence_number = self.series.get_next_sequence_number()

        self.slug = generate_slug_from_title(self)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        constraints = (
            UniqueConstraint(fields=['title', 'creator', ], name='unique_title_creator'),
            UniqueConstraint(fields=['series', 'series_sequence_number', ], name='unique_series_sequence_number'),
        )

    def swap_sequence_with(self, other_article: 'Article') -> Tuple['Article', 'Article']:
        if not self.series:
            raise ValueError("This article does not belong to a series.")
        return self.series.swap_article_sequence_numbers(self, other_article)


class Topic(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class ArticleSeries(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    description = models.TextField(verbose_name=_('Description'), blank=True, default='')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_title(self)
        super().save(*args, **kwargs)

    @transaction.atomic
    def swap_article_sequence_numbers(self, article_1: 'Article', article_2: 'Article') -> Tuple['Article', 'Article']:
        # TODO Fix the bug with unique together
        if article_1.series != article_2.series:
            raise ValueError("Both articles must belong to this series.")

        article_1.series_sequence_number, article_2.series_sequence_number = article_2.series_sequence_number, article_1.series_sequence_number
        Article.objects.bulk_update([article_1, article_2], ["series_sequence_number"])

        article_1.refresh_from_db()
        article_2.refresh_from_db()

        return article_1, article_2

    def get_next_sequence_number(self) -> int:
        max_sequence = self.articles.aggregate(max_seq=models.Max('series_sequence_number'))['max_seq']
        return (max_sequence or 0) + 1

    class Meta:
        verbose_name = _('Article Series')
        verbose_name_plural = _('Article Series')
