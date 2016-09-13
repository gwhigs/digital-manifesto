from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


@python_2_unicode_compatible
class Annotation(TimeStampedModel):
    user = models.ForeignKey(User)
    text_object = models.ForeignKey(settings.ANNOTATION_TEXT_OBJECT)

    # Key fields from the Annotator JSON Format: http://docs.annotatorjs.org/en/v1.2.x/annotation-format.html
    annotator_schema_version = models.CharField(max_length=8, blank=True)
    text = models.TextField(blank=True)
    quote = models.TextField()
    uri = models.URLField(blank=True)
    range_start = models.CharField(max_length=50, blank=True)
    range_end = models.CharField(max_length=50, blank=True)
    range_start_offset = models.BigIntegerField()
    range_end_offset = models.BigIntegerField()

    # Third party fields
    tags = TaggableManager(blank=True)

    def get_source_text(self):
        return getattr(self.text_object, 'text', '')

    def __str__(self):
        u = truncatechars(self.user.username, 15)
        t = truncatechars(self.text, 30)
        return '{}: "{}"'.format(u, t)
