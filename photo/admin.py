from django.contrib import admin
from .models import PhotoSessions, PhotoSessionsImage, salsi, Boat, City, Product, Client, PhotoTool, PhotoToolType, MoneyCurrency


class salsiAdmin(admin.ModelAdmin):
    model = salsi

    verbose_name = 'Продажи'
    verbose_name_plural = 'Продажи'

class PhotoToolAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'extension_number', 'DateEdit')


class MoneyCurrencyAdmin(admin.ModelAdmin):
    list_display = ('date_today', 'dollar', 'euro', 'rubl', 'grivna', 'funts')


class PhotoSessionsImageInline(admin.StackedInline):
    model = PhotoSessionsImage
    can_delete = False
    verbose_name_plural = 'Фото'


class PhotoSessionsAdmin(admin.ModelAdmin):
    inlines = (PhotoSessionsImageInline,)

admin.site.register(Client)

admin.site.register(Boat)

admin.site.register(City)

admin.site.register(Product)

admin.site.register(PhotoSessions, PhotoSessionsAdmin)

admin.site.register(PhotoTool, PhotoToolAdmin)

admin.site.register(PhotoToolType)

admin.site.register(MoneyCurrency, MoneyCurrencyAdmin)

admin.site.register(PhotoSessionsImage)

admin.site.register(salsi, salsiAdmin)