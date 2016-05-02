from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$',  ManifestoListView.as_view(), name='index'),
    url(r'^create/$', views.AnnotationCreateView.as_view(), name='create'),
]
