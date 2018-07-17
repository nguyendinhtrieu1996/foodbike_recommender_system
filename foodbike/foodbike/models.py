# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Food(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    menuid = models.ForeignKey('Menu', db_column='MenuId')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    desciption = models.CharField(db_column='Desciption', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Food'


class Menu(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    restaurantid = models.ForeignKey('Restaurant', db_column='RestaurantId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'


class Restaurant(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=256, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(db_column='Long', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat', blank=True, null=True)  # Field name made lowercase.
    opentime = models.TimeField(db_column='OpenTime', blank=True, null=True)  # Field name made lowercase.
    closetime = models.TimeField(db_column='CloseTime', blank=True, null=True)  # Field name made lowercase.
    openfromday = models.IntegerField(db_column='OpenFromDay', blank=True, null=True)  # Field name made lowercase.
    opentoday = models.IntegerField(db_column='OpenToDay', blank=True, null=True)  # Field name made lowercase.
    lowestprice = models.FloatField(db_column='LowestPrice')  # Field name made lowercase.
    highestprice = models.FloatField(db_column='HighestPrice')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Restaurant'


