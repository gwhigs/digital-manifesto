from django.views import generic

from . import models, mixins


class ManifestoListView(mixins.PrefetchRelatedMixin, generic.ListView):
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


class CollectionListView(generic.ListView):
    model = models.Collection


class CollectionDetailView(generic.DetailView):
    model = models.Collection