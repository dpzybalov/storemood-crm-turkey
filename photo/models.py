from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    fio = models.CharField(max_length=50, blank=True, default=None)
    telephone = models.CharField(max_length=15, blank=True, default=None)
    email = models.EmailField(blank=True, default=None)
    gorod = models.CharField(max_length=20, blank=True, default=None)
    date_prib = models.DateField

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class PhotoSessions(models.Model):
    title = models.CharField(max_length=50, blank=True)
    comment = models.TextField(blank=True)
    user = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=30, blank=True)
    boat = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=30, default='Новая')
    created_at = models.DateField(auto_now=True)
    Client = models.ManyToManyField(Client, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотосессия'
        verbose_name_plural = 'Фотосессии'

class salsi(models.Model):
    Photosessions = models.ForeignKey(PhotoSessions, on_delete=models.RESTRICT)
    images = models.FileField(upload_to= 'photos/', default=None)

    class Meta:
        verbose_name = 'Продажи'
        verbose_name_plural = 'Продажиe'


class PhotoSessionsImage(models.Model):
    Photosessions = models.ForeignKey(PhotoSessions, on_delete=models.RESTRICT)
    images = models.FileField(upload_to= 'photos/', default=None)


class City(models.Model):
    title = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Локации-города'
        verbose_name_plural = 'Локации-города'


class Boat(models.Model):
    title = models.CharField(max_length=30, db_index=True)
    city = models.ManyToManyField(City, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Яхта'
        verbose_name_plural = 'Список яхт'


class Product(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Список товаров'


class PhotoToolType(models.Model):
    title = models.CharField(max_length=30, verbose_name='Наименование')
    icon_type = models.CharField(max_length=30, blank=True, verbose_name='Иконка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Тип оборудования'


class PhotoTool(models.Model):
    title = models.CharField(max_length=30, verbose_name='Наименование')
    serial_number = models.CharField(max_length=30, verbose_name='Серийный номер')
    extension_number = models.CharField(max_length=30, verbose_name='Внутрений номер')
    Photo_tool_type = models.ForeignKey(PhotoToolType, on_delete=models.CASCADE, verbose_name='Тип техники')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Кому выдан')
    DateCreate = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    DateEdit = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class MoneyCurrency(models.Model):
    date_today = models.DateField(auto_now_add=True, editable=True, verbose_name='Дата')
    dollar = models.FloatField(max_length=5, verbose_name='Доллар')
    euro = models.FloatField(max_length=5, verbose_name='Евро')
    rubl = models.FloatField(max_length=5, verbose_name='Рубль')
    grivna = models.FloatField(max_length=5, verbose_name='Гривна')
    funts = models.FloatField(max_length=5, verbose_name='Фунты')

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курс валют'
