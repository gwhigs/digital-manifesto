from __future__ import absolute_import

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Manifesto, Collection

@admin.register(Manifesto)
class ManifestoAdmin(SimpleHistoryAdmin):
    search_fields = ('name',)
    list_display = ('name', )


admin.site.register(Collection)