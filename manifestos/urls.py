from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ManifestoListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ManifestoDetailView.as_view(), name='detail'),
]
