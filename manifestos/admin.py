from __future__ import absolute_import

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Manifesto, Collection, Tweet


@admin.register(Manifesto)
class ManifestoAdmin(SimpleHistoryAdmin):
    search_fields = ('name',)
    list_display = ('name', )


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = (
        'name',
        'description',
        'creator',
        'contributor',
        'subject',
        'art_file',
        'featured',
    )


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('modified', 'tweeted', 'text')
    fields = ('text',)
    search_fields = ('text',)
    ordering = ('modified',)
