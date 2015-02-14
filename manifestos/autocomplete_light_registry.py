from __future__ import absolute_import, unicode_literals

import autocomplete_light
from taggit.models import Tag

from .models import Manifesto, Collection

# Taggit integration
autocomplete_light.register(
    Tag,
    attrs={
        'placeholder': 'Start typing to search.'
    }
)
# This will generate and register a ShowAutocomplete class
autocomplete_light.register(
    Manifesto,
    # Just like in ModelAdmin.search_fields
    search_fields=['name'],
    # For javascript attribute widget.autocomplete.placeholder
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Search Manifestos',
    },
)

# This will generate and register a HostAutocomplete class
autocomplete_light.register(
    Collection,
    search_fields=['name'],
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Search Collections',
    },
)
