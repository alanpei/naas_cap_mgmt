from django.contrib import admin
from nuage.models import *
# Register your models here.
class NsgLicensesModelAdmin(admin.ModelAdmin):
    list_display = ('vsd_id', 'lic_total', 'lic_used')
class VscEsxiCapModelAdmin(admin.ModelAdmin):
    list_display = ('vsc_pod_id','vsc_pod_name','host_count','vsc_count','vsc_cap')
    search_fields = ('vsc_pod_name', )
    ordering = ('vsc_pod_id', )



admin.site.register(NsgLicenses,NsgLicensesModelAdmin)
admin.site.register(VscEsxiCap,VscEsxiCapModelAdmin)
admin.site.register(EsStorage)
admin.site.register(IdcCpuCap)
admin.site.register(NfvCpuCap)




admin.site.site_header = 'TELUS NaaS Capacity Management Tool'
admin.site.index_title = 'TELUS NaaS Capacity'
admin.site.site_title = 'NaaS Admin Tool'
