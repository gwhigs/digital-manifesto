from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Prefetch

from braces.views import PrefetchRelatedMixin

from annotations.forms import AnnotationForm
from . import models


class ManifestoListView(PrefetchRelatedMixin, generic.ListView):
    model = models.Manifesto
    prefetch_related = ['tags']
    queryset = models.Manifesto.objects.defer('text')


class ManifestoDetailView(generic.DetailView):
    model = models.Manifesto

    def get_context_data(self, **kwargs):
        context = super(ManifestoDetailView, self).get_context_data(**kwargs)
        # Add an Annotation creation form to our template context
        initial = {
            'user': self.request.user,
            'manifesto': self.object,
        }
        context['form'] = AnnotationForm(initial=initial)
        context['storage_api_base_url'] = reverse('annotations:api:index')[:-1]
        return context


class CollectionListView(generic.ListView):
    model = models.Collection
    prefetch_qs = models.Manifesto.objects.defer('text')
    prefetch = Prefetch('manifesto_set', queryset=prefetch_qs)
    queryset = models.Collection.objects.prefetch_related(prefetch)


class CollectionDetailView(PrefetchRelatedMixin, generic.DetailView):
    model = models.Collection
    prefetch_related = ['manifesto_set', 'manifesto_set__tags']
