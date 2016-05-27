from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from . import models


@admin.register(models.Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    fields = (
        'user',
        'text_object',
        'annotator_schema_version',
        'text',
        'quote',
        'uri',
        'range_start',
        'range_end',
        'range_start_offset',
        'range_end_offset',
        'tags',
    )
