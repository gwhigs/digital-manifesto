from __future__ import unicode_literals
from django.contrib import messages

from django.core.exceptions import ImproperlyConfigured
from django.db import models


class PrefetchRelatedMixin(object):
    """
    Allows a CBV to use prefetch_related on their queryset.
    """
    prefetch_related = None

    def get_queryset(self):
        if self.prefetch_related is None:
            msg = ('{} is missing the prefetch_related property. This must '
                   'be a tuple or list.').format(self.__class__.__name__)
            raise ImproperlyConfigured(msg)

        if not isinstance(self.prefetch_related, (tuple, list)):
            msg = ("{}'s prefetch_related property "
                   'must be a tuple or list.').format(self.__class__.__name__)
            raise ImproperlyConfigured(msg)

        queryset = super(PrefetchRelatedMixin, self).get_queryset()
        return queryset.prefetch_related(*self.prefetch_related)


class SelectRelatedMixin(object):
    """
    Allows a CBV to use select_related on their queryset.
    """
    select_related = None

    def get_queryset(self):
        if self.select_related is None:
            msg = ('{} is missing the select_related property. This must '
                   'be a tuple or list.').format(self.__class__.__name__)
            raise ImproperlyConfigured(msg)

        queryset = super(SelectRelatedMixin, self).get_queryset()

        return queryset.select_related(self.select_related)


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