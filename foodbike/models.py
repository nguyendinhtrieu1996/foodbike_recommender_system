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
    name = models.CharField(db_column='Name')  # Field name made lowercase.
    description = models.CharField(db_column='Description')  # Field name made lowercase.
    defaultimage = models.CharField(db_column='DefaultImage')  # Field name made lowercase.
    menuid = models.ForeignKey('Menu', db_column='MenuId')  # Field name made lowercase.
    status = models.BooleanField(db_column='Status')  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate')  # Field name made lowercase.
    lastupdate = models.DateField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Food'


class Menu(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    restaurantid = models.ForeignKey('Restaurant', db_column='RestaurantId')  # Field name made lowercase.
    name = models.CharField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'


class Restaurant(models.Model):
    userid = models.CharField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name')  # Field name made lowercase.
    status = models.CharField(db_column='Status')  # Field name made lowercase.
    opentime = models.TimeField(db_column='OpenTime')  # Field name made lowercase.
    closetime = models.TimeField(db_column='CloseTime')  # Field name made lowercase.
    long = models.FloatField(db_column='Long')  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    description = models.CharField(db_column='Description')  # Field name made lowercase.
    type = models.CharField(db_column='Type')  # Field name made lowercase.
    openfromday = models.IntegerField(db_column='OpenFromDay')  # Field name made lowercase.
    opentoday = models.IntegerField(db_column='OpenToDay')  # Field name made lowercase.
    highestprice = models.FloatField(db_column='HighestPrice')  # Field name made lowercase.
    lowestprice = models.FloatField(db_column='LowestPrice')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Restaurant'


class Banner(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image')  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate')  # Field name made lowercase.
    lastupdate = models.DateField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Banner'


class Userdetail(models.Model):
    userid = models.CharField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName')  # Field name made lowercase.
    address = models.CharField(db_column='Address')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber')  # Field name made lowercase.
    deleteflag = models.IntegerField(db_column='DeleteFlag')  # Field name made lowercase.
    avartar = models.CharField(db_column='Avartar')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate')  # Field name made lowercase.
    email = models.CharField(db_column='Email')  # Field name made lowercase.
    isphoneverify = models.BooleanField(db_column='IsPhoneVerify')  # Field name made lowercase.
    loginprovider = models.CharField(db_column='LoginProvider')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserDetail'
