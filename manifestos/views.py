from django.views import generic
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
        return context


class CollectionListView(PrefetchRelatedMixin, generic.ListView):
    model = models.Collection
    prefetch_related = ['manifestos']


class CollectionDetailView(PrefetchRelatedMixin, generic.DetailView):
    model = models.Collection
    prefetch_related = ['manifestos', 'manifestos__tags']