# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0002_auto_20150215_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='creator',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='subject',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
