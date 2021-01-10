from django.contrib import admin
from .models import PhotoSessions, Boat, City, Product, Client, PhotoTool, PhotoToolType, MoneyCurrency


class PhotoToolAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'extension_number', 'DateEdit')

class MoneyCurrencyAdmin(admin.ModelAdmin):
    list_display = ('date_today', 'dollar', 'euro', 'rubl', 'grivna', 'funts')


admin.site.register(Client)

admin.site.register(PhotoSessions)

admin.site.register(Boat)

admin.site.register(City)

admin.site.register(Product)

admin.site.register(PhotoTool, PhotoToolAdmin)

admin.site.register(PhotoToolType)

admin.site.register(MoneyCurrency, MoneyCurrencyAdmin)
