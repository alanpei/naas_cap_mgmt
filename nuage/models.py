# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EsStorage(models.Model):
    es_id = models.IntegerField(primary_key=True)
    storage_total = models.FloatField(blank=True, null=True)
    storage_used = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_storage'


class IdcCpuCap(models.Model):
    idc_pod_id = models.IntegerField(blank=True, null=True)
    idc_pod_name = models.CharField(max_length=10, blank=True, null=True)
    cpu_total = models.FloatField(blank=True, null=True)
    cpu_used = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idc_cpu_cap'


class NfvCpuCap(models.Model):
    nfv_pod_id = models.IntegerField(primary_key=True)
    nfv_pod_name = models.CharField(max_length=10, blank=True, null=True)
    cpu_total = models.SmallIntegerField(blank=True, null=True)
    cpu_used = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nfv_cpu_cap'


class NsgLicenses(models.Model):
    vsd_id = models.IntegerField(primary_key=True)
    lic_total = models.SmallIntegerField(blank=True, null=True)
    lic_used = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nsg_licenses'


class VscEsxiCap(models.Model):
    vsc_pod_id = models.IntegerField(primary_key=True)
    vsc_pod_name = models.CharField(max_length=8, blank=True, null=True)
    host_count = models.IntegerField(blank=True, null=True)
    vsc_count = models.IntegerField(blank=True, null=True)
    vsc_cap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vsc_esxi_cap'
