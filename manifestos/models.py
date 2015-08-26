from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager
import sorl.thumbnail
from featureditem.fields import FeaturedField


class Collection(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    creator = models.TextField(blank=True)
    contributor = models.TextField(blank=True)
    subject = models.TextField(blank=True)
    art_height = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text='automatically populated when file is uploaded, leave blank'
    )
    art_width = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text='automatically populated when file is uploaded, leave blank'
    )
    art_file = sorl.thumbnail.ImageField(
        'splash art file',
        upload_to='img',
        blank=True,
        width_field='art_width',
        height_field='art_height',
    )
    featured = FeaturedField()

    def get_absolute_url(self):
        return reverse('manifestos:collection_detail', args=[str(self.id)])

    def get_most_recent_manifesto(self):
        return self.manifesto_set.first()

    @python_2_unicode_compatible
    def __str__(self):
        return self.name


class Manifesto(TimeStampedModel):
    name = models.CharField(max_length=255)  # needs html tag functionality
    creator = models.TextField(blank=True)
    date = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)  # needs html tag functionality
    art_height = models.PositiveSmallIntegerField(blank=True, null=True)
    art_width = models.PositiveSmallIntegerField(blank=True, null=True)
    art_file = sorl.thumbnail.ImageField(
        'splash art file',
        upload_to='img',
        blank=True,
        width_field='art_width',
        height_field='art_height',
    )
    duration = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=7, choices=settings.LANGUAGES, default='en')
    publisher = models.CharField(blank=True, max_length=255)  # needs html tag functionality
    rights = models.TextField(blank=True)  # needs html tag functionality
    source = models.URLField(blank=True)
    added = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)  # needs html tag functionality
    collection = models.ForeignKey(Collection, null=True, blank=True)
    featured = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    featured = FeaturedField()
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('manifestos:detail', args=[str(self.id)])

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-added']