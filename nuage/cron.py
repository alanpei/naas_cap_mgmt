from nuage.models import NsgLicenses, EsStorage, IdcCpuCap, NfvCpuCap, VscEsxiCap

def update_nsg_licenses():
    nsgLicense = NsgLicenses.objects.get(vsd_id=1)
    nsgLicense.lic_used = 3000
    nsgLicense.lic_total = 6000
    nsgLicense.save()
    print("NSG Licenses are updated")

def update_es_storage():

    esStorage = EsStorage.objects.get(es_id=1)
    esStorage.storage_total = 14.6
    esStorage.storage_used = 3.0
    esStorage.save()
    print("ES disk usages are updated")

def update_idc_cpu_cap():
    print("IDC capacity are updated")

def update_nfv_cpu_cap():
    print("NFV capacity are updated")

def update_vsc_esxi_cap():
    print("VSC ESXi capacity are updated")
