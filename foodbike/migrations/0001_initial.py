# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('name', models.CharField(max_length=256, null=True, db_column='Name', blank=True)),
                ('status', models.IntegerField(null=True, db_column='Status', blank=True)),
                ('desciption', models.CharField(max_length=256, null=True, db_column='Desciption', blank=True)),
            ],
            options={
                'db_table': 'Food',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('name', models.CharField(max_length=256, null=True, db_column='Name', blank=True)),
            ],
            options={
                'db_table': 'Menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='Id')),
                ('name', models.CharField(max_length=256, null=True, db_column='Name', blank=True)),
                ('address', models.CharField(max_length=256, null=True, db_column='Address', blank=True)),
                ('description', models.CharField(max_length=256, null=True, db_column='Description', blank=True)),
                ('long', models.FloatField(null=True, db_column='Long', blank=True)),
                ('lat', models.FloatField(null=True, db_column='Lat', blank=True)),
                ('opentime', models.TimeField(null=True, db_column='OpenTime', blank=True)),
                ('closetime', models.TimeField(null=True, db_column='CloseTime', blank=True)),
                ('openfromday', models.IntegerField(null=True, db_column='OpenFromDay', blank=True)),
                ('opentoday', models.IntegerField(null=True, db_column='OpenToDay', blank=True)),
                ('lowestprice', models.FloatField(db_column='LowestPrice')),
                ('highestprice', models.FloatField(db_column='HighestPrice')),
                ('status', models.IntegerField(db_column='Status')),
            ],
            options={
                'db_table': 'Restaurant',
                'managed': False,
            },
        ),
    ]
