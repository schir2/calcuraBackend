from django.db import models
from django.utils.translation import gettext_lazy as _
from django_currentuser.db.models import CurrentUserField


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    edited_at = models.DateTimeField(verbose_name=_('Edited At'), auto_now=True)
    creator = CurrentUserField(verbose_name=_('Creator'), on_update=False, on_delete=models.CASCADE,
                               related_name='created_%(class)s')
    editor = CurrentUserField(verbose_name=_('Editor'), on_update=True, on_delete=models.CASCADE,
                              related_name='edited_%(class)s')

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['edited_at']),
            models.Index(fields=['creator']),
            models.Index(fields=['editor']),
        ]
        ordering = ['-created_at']