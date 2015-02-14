# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0004_auto_20150112_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifesto',
            name='creator',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
