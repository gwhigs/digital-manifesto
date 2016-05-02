from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from manifestos.models import Manifesto


class Annotation(TimeStampedModel):
    user = models.ForeignKey(User)
    text_object = models.ForeignKey(Manifesto)
    text_start_index = models.PositiveIntegerField()
    text_end_index = models.PositiveIntegerField()
    text = models.TextField(blank=True)
    history = HistoricalRecords()

    def get_source_text(self):
        return getattr(self.text_object, 'text', '')

    def clean(self):
        if self.text_end_index < self.text_start_index:
            raise ValidationError(
                "Text indices don't make sense. Check you selection tool."
            )
        if self.text_end_index < len(self.get_source_text()):
            raise ValidationError('Index outside text range.')

    def get_absolute_url(self):
        return reverse('manifestos:detail', args=[str(self.text_object.pk)])

    @python_2_unicode_compatible
    def __str__(self):
        u = truncatechars(self.user.username, 15)
        t = truncatechars(self.text, 30)
        return '{}: "{}"'.format(u, t)
