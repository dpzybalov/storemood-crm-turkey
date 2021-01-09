"""storemoodcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.urls import path, include
from login.views import user_login, user_logout, user_profile
from photo.views import index_photo, add_photosession
from avatar import urls
from django.contrib.auth import views
from django.contrib import redirects



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login),
    path('logout', user_logout),
    path('photo/', index_photo),
    path('profile/', user_profile),
    path('photo/add-photosession', add_photosession),
    url('avatar/', include('avatar.urls')),
    path('password-reset/', views.PasswordResetView.as_view(template_name="password_reset_form.html"), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

