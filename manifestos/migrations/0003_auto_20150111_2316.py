# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0002_auto_20150111_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifesto',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
