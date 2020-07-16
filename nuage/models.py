# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EsStorage(models.Model):
    es_id = models.IntegerField(primary_key=True, verbose_name='ES ID')
    storage_total = models.FloatField(blank=True, null=True, verbose_name='ES Total Space')
    storage_used = models.FloatField(blank=True, null=True, verbose_name='ES Used Space')

    class Meta:
        managed = False
        db_table = 'es_storage'
        verbose_name = 'ES Capacity'
        verbose_name_plural = 'ES Capacity'


class IdcCpuCap(models.Model):
    idc_pod_id = models.IntegerField(primary_key=True)
    idc_pod_name = models.CharField(max_length=10, blank=True, null=True)
    cpu_total = models.SmallIntegerField(blank=True, null=True)
    cpu_used = models.SmallIntegerField(blank=True, null=True)
    # idc_pod_id = models.IntegerField(blank=True, null=True, verbose_name='POD ID')
    # idc_pod_name = models.CharField(max_length=10, blank=True, null=True, verbose_name='IDC POD NAME')
    # cpu_total = models.FloatField(blank=True, null=True, verbose_name='IDC Total Cores')
    # cpu_used = models.FloatField(blank=True, null=True, verbose_name='IDC Used Cores')
    class Meta:
        managed = False
        db_table = 'idc_cpu_cap'
        # verbose_name = 'IDC Capacity'
        # verbose_name_plural = 'IDC Capacity'


class NfvCpuCap(models.Model):
    nfv_pod_id = models.IntegerField(primary_key=True, verbose_name='POD ID')
    nfv_pod_name = models.CharField(max_length=10, blank=True, null=True, verbose_name='NFV POD Name')
    cpu_total = models.SmallIntegerField(blank=True, null=True, verbose_name='NFV CPU total')
    cpu_used = models.SmallIntegerField(blank=True, null=True, verbose_name='NFV CPU used')

    class Meta:
        managed = False
        db_table = 'nfv_cpu_cap'
        verbose_name = 'NFV RGv Capacity'
        verbose_name_plural = 'NFV RGv Capacity'


class NsgLicenses(models.Model):
    vsd_id = models.IntegerField(primary_key=True, verbose_name='VSD ID')
    lic_total = models.SmallIntegerField(blank=True, null=True, verbose_name='Total NSG Licenses')
    lic_used = models.SmallIntegerField(blank=True, null=True, verbose_name='NSG activated')

    class Meta:
        managed = False
        db_table = 'nsg_licenses'
        verbose_name = 'NSG Licenses'
        verbose_name_plural = 'NSG Licenses'


class VscEsxiCap(models.Model):
    vsc_pod_id = models.IntegerField(primary_key=True, verbose_name='POD ID')
    vsc_pod_name = models.CharField(max_length=8, blank=True, null=True, verbose_name='VSC Location')
    host_count = models.IntegerField(blank=True, null=True, verbose_name='ESXi hosts')
    vsc_count = models.IntegerField(blank=True, null=True, verbose_name='VSC Current#')
    vsc_cap = models.IntegerField(blank=True, null=True, verbose_name='VSC Max#')

    class Meta:
        managed = False
        db_table = 'vsc_esxi_cap'
        verbose_name = 'VSC ESXi Capacity'
        verbose_name_plural = 'VSC ESXi Capacity'
