# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import featureditem.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0004_auto_20150513_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='art_file',
            field=sorl.thumbnail.fields.ImageField(height_field='art_height', upload_to='img', width_field='art_width', verbose_name='splash art file', blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='art_height',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='art_width',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='featured',
            field=featureditem.fields.FeaturedField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalmanifesto',
            name='featured',
            field=featureditem.fields.FeaturedField(default=False),
        ),
        migrations.AlterField(
            model_name='manifesto',
            name='featured',
            field=featureditem.fields.FeaturedField(default=False),
        ),
    ]
