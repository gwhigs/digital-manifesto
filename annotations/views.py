from __future__ import absolute_import, unicode_literals
from rest_framework import permissions, viewsets, views, parsers, renderers, filters

from . import models, serializers


class AnnotationRenderer(renderers.JSONRenderer):
    """
    Format our JSON response so Annotator JS will recognize it.
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, (list, tuple)):
            data = {'rows': data}
        return super(AnnotationRenderer, self).render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)


class AnnotationViewSet(viewsets.ModelViewSet):
    """
    View to handle all Annotator JS requests
    """
    queryset = models.Annotation.objects.defer('text_object__text').select_related('text_object')
    serializer_class = serializers.AnnotationSerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.JSONParser,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('text_object_id', 'uri')
    renderer_classes = (AnnotationRenderer, renderers.BrowsableAPIRenderer)


class AnnotationIndexAPI(views.APIView):
    """
    Placeholder view for use in `urlpatterns` so we can `reverse()` our API endpoint
    """
    pass
