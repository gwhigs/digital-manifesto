from __future__ import absolute_import, unicode_literals

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'