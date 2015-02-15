# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manifesto',
            options={'ordering': ['-added']},
        ),
        migrations.AlterField(
            model_name='manifesto',
            name='art_file',
            field=sorl.thumbnail.fields.ImageField(upload_to='img', width_field='art_width', blank=True, height_field='art_height', verbose_name='splash art file'),
            preserve_default=True,
        ),
    ]
