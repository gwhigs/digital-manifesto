"""
All urls for the Annotations API go here.
"""

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

from rest_framework import routers

# The rest_framework router creates all the URLs we need by default.
# See http://www.django-rest-framework.org/api-guide/routers/
# or check out the docs/ below for details on default name structures
router = routers.SimpleRouter()
router.register(r'annotations', views.AnnotationViewSet)

urlpatterns = router.urls

urlpatterns += (
    url(r'^$', views.AnnotationIndexAPI.as_view(), name='index'),
    # Optional 3rd party generated documentation
    # url(r'^docs/', include('rest_framework_swagger.urls')),
)
