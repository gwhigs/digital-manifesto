from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager


class Collection(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    contributor = models.TextField(blank=True)


class Manifesto(TimeStampedModel):
    name = models.CharField(max_length=255)
    creator = models.TextField(blank=True)
    date = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    art_height = models.PositiveSmallIntegerField(blank=True, null=True)
    art_width = models.PositiveSmallIntegerField(blank=True, null=True)
    art_file = models.ImageField(
        'splash art file',
        upload_to='img',
        blank=True,
        width_field='art_width',
        height_field='art_height',
    )
    duration = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=7, choices=settings.LANGUAGES, default='en')
    publisher = models.CharField(blank=True, max_length=255)
    rights = models.TextField(blank=True)
    source = models.URLField(blank=True)
    added = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    collection = models.ForeignKey(Collection, null=True, blank=True)
    featured = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    history = HistoricalRecords()