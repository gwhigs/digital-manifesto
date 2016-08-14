from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.generic import TemplateView

from manifestos.models import Collection


LETSENCRYPT_SECRET = 'RoqK1ZHN6384upsmMKbrJuxqaGNKcmJc5JApOy8qi8Y'


def acme_challenge(request, key):
    resp = '.'.join((key, LETSENCRYPT_SECRET))
    return HttpResponse(resp)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['collection'] = Collection.objects.get(featured=True)
        return context
