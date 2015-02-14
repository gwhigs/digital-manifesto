# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0003_auto_20150111_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifesto',
            name='rights',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
