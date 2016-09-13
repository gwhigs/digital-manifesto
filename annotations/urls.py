from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from . import views, api_urls

urlpatterns = [
    url(r'^api/', include(api_urls, namespace='api'))
]
