from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # Admin
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Simple template views
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^news/$', TemplateView.as_view(template_name='news.html'), name='news'),
    url(r'^projects-we-like/$', TemplateView.as_view(template_name='projects_we_like.html'), name='projects'),
    url(r'^resources/$', TemplateView.as_view(template_name='resources.html'), name='resources'),
    url(r'^manifestos/', include('manifestos.urls', namespace='manifestos')),
    url(r'^annotations/', include('annotations.urls', namespace='annotations')),

    # Let's Encrypt challenge
    url(r'^.well-known/acme-challenge/(?P<key>.*)/', views.acme_challenge),

    # allauth
    url(r'^accounts/', include('allauth.urls')),
]
