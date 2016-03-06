# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0006_auto_20160306_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ('-modified',)},
        ),
    ]
