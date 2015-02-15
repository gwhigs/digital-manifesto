from django.views import generic

from . import models


class ManifestoListView(generic.ListView):
    model = models.Manifesto


class ManifestoDetailView(generic.DetailView):
    model = models.Manifesto