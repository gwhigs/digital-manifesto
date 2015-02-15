from django.views import generic

from . import models, mixins


class ManifestoListView(mixins.PrefetchRelatedMixin, generic.ListView):
    model = models.Manifesto
    prefetch_related = ['tags']


class ManifestoDetailView(generic.DetailView):
    model = models.Manifesto