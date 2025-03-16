from rest_framework import viewsets

from blog.models import Article, Topic, Tag, ArticleSeries
from blog.serializers import ArticleSerializer, TopicSerializer, TagSerializer, ArticleSeriesSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().select_related('creator')
    serializer_class = ArticleSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().select_related('creator')
    serializer_class = TopicSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().select_related('creator')
    serializer_class = TagSerializer


class ArticleSeriesViewSet(viewsets.ModelViewSet):
    queryset = ArticleSeries.objects.all().select_related('creator')
    serializer_class = ArticleSeriesSerializer