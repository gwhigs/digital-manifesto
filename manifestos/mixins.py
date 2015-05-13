from __future__ import unicode_literals
from django.contrib import messages

from django.db import models


class ContactInfoMixin(models.Model):
    """
    Adds contact info fields to a model.
    """

    email = models.EmailField(blank=True)
    phone = models.CharField('phone number', max_length=25, blank=True)
    address_1 = models.CharField('address', max_length=63, blank=True)
    address_2 = models.CharField('address line 2', max_length=63, blank=True)
    city = models.CharField(max_length=63, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField('zip code', max_length=10, blank=True)

    def save(self, *args, **kwargs):
        # State should be saved in caps
        if self.state:
            self.state = self.state.upper()
        super(ContactInfoMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class SuccessMessageMixin(object):
    """
    A mixin for gathering code that is common to create and update views.
    """

    exclude = []

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(SuccessMessageMixin, self).form_valid(form)