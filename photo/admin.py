from django.contrib import admin
from .models import PhotoSessions, boat, city, product, client, PhotoTool, PhotoToolType, money_currency


class PhotoToolAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'extension_number', 'DateEdit')

class money_currencyAdmin(admin.ModelAdmin):
    list_display = ('date_today', 'dollar', 'euro', 'rubl', 'grivna', 'funts')


admin.site.register(client)

admin.site.register(PhotoSessions)

admin.site.register(boat)

admin.site.register(city)

admin.site.register(product)

admin.site.register(PhotoTool, PhotoToolAdmin)

admin.site.register(PhotoToolType)

admin.site.register(money_currency, money_currencyAdmin)
