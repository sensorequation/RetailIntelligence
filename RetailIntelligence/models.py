# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    addrress_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postalcode = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Costco(models.Model):
    itemid = models.IntegerField(blank=True, null=True)
    productid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costco'


class Device(models.Model):
    deviceid = models.IntegerField(db_column='deviceID', blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='warehouseID', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(max_length=255, blank=True, null=True)
    macaddress = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'


class Nfcinfo(models.Model):
    nfc_id = models.IntegerField()
    company = models.ForeignKey(Company, models.DO_NOTHING)
    nfc_size = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nfcinfo'


class Offer(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    offer_url = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer'


class Warehouse(models.Model):
    warehouseid = models.IntegerField(db_column='warehouseID', blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(max_length=255, blank=True, null=True)
    postalcode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse'
