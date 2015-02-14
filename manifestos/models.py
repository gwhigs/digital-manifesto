from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Collection(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Subject(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Manifesto(TimeStampedModel):
    name = models.CharField(max_length=255)
    creator = models.TextField(blank=True)
    date = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=7, choices=settings.LANGUAGES, default='en')
    publisher = models.CharField(blank=True, max_length=255)
    rights = models.TextField(blank=True)
    source = models.URLField(blank=True)
    added = models.DateTimeField(null=True, blank=True)
    subject = models.ManyToManyField(Subject, blank=True)
    text = models.TextField(blank=True)
    collection = models.ForeignKey(Collection, null=True, blank=True)
    featured = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
