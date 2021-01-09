from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'get_city')


class UserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)
    list_display = ('username', 'first_name', 'last_name')


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(Profile, ProfileAdmin)
