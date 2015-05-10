from django.views import generic
from braces.views import SelectRelatedMixin, PrefetchRelatedMixin

from . import models


class ManifestoListView(PrefetchRelatedMixin, generic.ListView):
    model = models.Manifesto
    prefetch_related = ['tags']
    queryset = models.Manifesto.objects.defer('text')
    #     'text',
    #     'art_file',
    #     'tags',
    #     'description',
    #
    # )


class ManifestoDetailView(generic.DetailView):
    model = models.Manifesto


class CollectionListView(PrefetchRelatedMixin, generic.ListView):
    model = models.Collection
    prefetch_related = ['manifesto_set']


class CollectionDetailView(PrefetchRelatedMixin, generic.DetailView):
    model = models.Collection
    prefetch_related = ['manifesto_set', 'manifesto_set__tags']