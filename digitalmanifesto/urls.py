from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutTemplateView.as_view(), name='about'),
    url(r'^contact/$', views.ContactTemplateView.as_view(), name='contact'),
    url(r'^news/$', views.NewsTemplateView.as_view(), name='news'),
    url(r'^projects-we-like/$', views.ProjectsTemplateView.as_view(), name='projects'),
    url(r'^resources/$', views.ResourcesTemplateView.as_view(), name='resources'),
    url(r'^manifestos/', include('manifestos.urls', namespace='manifestos')),
]
