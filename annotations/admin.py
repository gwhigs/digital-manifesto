from django.contrib import admin

from . import models


@admin.register(models.Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    fields = ('__all__',)
