from django.contrib import admin
from .models import *
class TariffAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')
admin.site.register(Tariff, TariffAdmin)
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
admin.site.register(Banner, BannerAdmin)
