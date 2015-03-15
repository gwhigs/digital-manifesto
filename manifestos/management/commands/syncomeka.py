from __future__ import unicode_literals

from dateutil import parser
from django.core.files.base import ContentFile
import requests

from django.core.management.base import NoArgsCommand
from django.utils.html import strip_tags

from manifestos import models
from manifestos import apitools


# Custom conversion functions for model fields below


def convert_featured(s):
    if isinstance(s, bool):
        return s
    elif isinstance(s, str):
        return s.lower() == 'true'
    else:
        return False


def convert_date(s):
    return parser.parse(s)


def get_collection(_id):
    return models.Collection.objects.get(id=_id)


def get_file_tuple(api_url):
    r = requests.get(api_url)
    try:
        file_url = r.json()[0].get('file_urls', {}).get('original')
    except IndexError:
        return None, None
    if file_url:
        fn = file_url.split('?')[0].split('/')[-1]
        r_file = requests.get(file_url)
        r_file.raise_for_status()
        file = ContentFile(r_file.content)
        return fn, file
    return None, None


# Which models to sync. Should be a list of three-tuples, with fields
# (
# omeka_resource_name,
# django_model,
# {
# omeka_field: (django_field, omeka_to_django_conversion_callable)
# }
# )
SYNC_MODELS = [
    (
        'collections',
        models.Collection,
        {
            'id': ('id', int),
            'Title': ('name', strip_tags),
            'added': ('added', convert_date),
            'Description': ('description', strip_tags),
            'Contributor': ('contributor', strip_tags),

        }
    ),
    (
        'items',  # Omeka resource name
        models.Manifesto,  # Django model
        {  # A list of Omeka fields in the resource. Must contain 'id' as int
           'id': ('id', int),
           'Title': ('name', strip_tags),  # (django_field_name, conversion_func)
           'Creator': ('creator', strip_tags),
           'Date': ('date', None),
           'Description': ('description', None),
           'Duration': ('duration', None),
           'Language': ('language', str.lower),
           'Publisher': ('publisher', None),
           'Rights': ('rights', strip_tags),
           'Source': ('source', strip_tags),
           'added': ('added', convert_date),
           'Subject': ('subject', None),
           'Text': ('text', None),
           'featured': ('featured', convert_featured),
           'tags': ('tags', None),
           'collection_id': ('collection', get_collection),
           'files_url': ('file', get_file_tuple),
        }
    ),
]


def make_model_dict(omeka_obj, sync_dict):
    """
    Constructs a model dict from an Omeka object, using a correctly formatted
    syncing dict. Sync dict is the third tuple item in SYNC_MODELS.
    """
    d = {}
    for key, (field, conv_func) in sync_dict.items():
        omeka = omeka_obj.get(key)
        if omeka:
            d[field] = conv_func(omeka) if conv_func else omeka
    return d


class Command(NoArgsCommand):
    help = ("Syncs to the project's Omeka database.")

    def handle_noargs(self, **options):
        for (resource, model, sync_dict) in SYNC_MODELS:
            # Get data from Omeka
            omeka_data = apitools.get_all(resource)
            # Handle Omeka data
            omeka_handled = apitools.handle_omeka(omeka_data)
            for omeka_obj in omeka_handled:
                obj_dict = make_model_dict(omeka_obj, sync_dict)
                if not isinstance(obj_dict['id'], int):
                    print('{} not made'.format(obj_dict['name']))
                    continue

                # Pop out tags, to handle them specially later
                tag_list = obj_dict.pop('tags', [])
                tags = [tag.get('name') for tag in tag_list]

                # Also pop out file objects, same thing
                fn, file = obj_dict.pop('file', (None, None))
                obj, created = model.objects.get_or_create(id=obj_dict['id'])
                for key, value in obj_dict.items():
                    setattr(obj, key, value)
                if tags:
                    obj.tags.add(*tags)
                if file:
                    obj.art_file.save(fn, file)
                obj.save()
                action = 'created' if created else 'updated'
                self.stdout.write('Object {}: {}'.format(action, obj.name))