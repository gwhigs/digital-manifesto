# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifesto',
            name='added',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
