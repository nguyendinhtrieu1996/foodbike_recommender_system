# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_auto_20180714_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='content_id',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='log',
            name='user_id',
            field=models.CharField(max_length=128),
        ),
    ]
