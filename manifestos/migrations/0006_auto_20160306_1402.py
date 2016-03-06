# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0005_auto_20150825_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', models.CharField(max_length=140)),
                ('tweeted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='collection',
            name='art_height',
            field=models.PositiveSmallIntegerField(blank=True, null=True, help_text='automatically populated when file is uploaded, leave blank'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='art_width',
            field=models.PositiveSmallIntegerField(blank=True, null=True, help_text='automatically populated when file is uploaded, leave blank'),
        ),
    ]
