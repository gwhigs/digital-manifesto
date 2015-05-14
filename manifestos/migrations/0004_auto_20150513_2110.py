# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('manifestos', '0003_auto_20150509_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalmanifesto',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical manifesto'},
        ),
        migrations.RemoveField(
            model_name='historicalmanifesto',
            name='collection_id',
        ),
        migrations.AddField(
            model_name='historicalmanifesto',
            name='collection',
            field=models.ForeignKey(db_constraint=False, blank=True, related_name='+', to='manifestos.Collection', null=True, on_delete=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AlterField(
            model_name='historicalmanifesto',
            name='history_user',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
