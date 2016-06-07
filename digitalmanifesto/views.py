from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.generic import TemplateView

from manifestos.models import Manifesto, Collection


LETSENCRYPT_SECRET = 'ZgmyqfB2TZhlMSqwc2-4gJdLgpJzh_qTZxapNDNI2fk.RoqK1ZHN6384upsmMKbrJuxqaGNKcmJc5JApOy8qi8Y'


def acme_challenge(request):
    return HttpResponse(LETSENCRYPT_SECRET)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['collection'] = Collection.objects.get(featured=True)
        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class NewsTemplateView(TemplateView):
    template_name = 'news.html'


class ProjectsTemplateView(TemplateView):
    template_name = 'projects_we_like.html'


class ResourcesTemplateView(TemplateView):
    template_name = 'resources.html'