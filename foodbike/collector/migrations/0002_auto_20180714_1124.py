# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='session_inx',
        ),
        migrations.RemoveField(
            model_name='log',
            name='visit_count',
        ),
        migrations.AlterField(
            model_name='log',
            name='content_id',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='log',
            name='user_id',
            field=models.CharField(max_length=16),
        ),
    ]
