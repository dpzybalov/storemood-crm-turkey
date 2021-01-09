from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class client(models.Model):
    fio = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    gorod = models.CharField(max_length=20)
    date_prib = models.DateField

    class Meta:
        verbose_name = ('Клиент')
        verbose_name_plural = ('Клиенты')



class PhotoSessions(models.Model):
    title = models.CharField(max_length=50, blank=True)
    comment = models.TextField(blank=True)
    user = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    photos = models.FileField(upload_to='photos/%d/%m/%Y/', blank=True)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    boat = models.ForeignKey('Boat', on_delete=models.PROTECT)
    status = models.CharField(max_length=30, default='Новая')
    created_at = models.DateField(auto_now=True)
    client = models.ManyToManyField(client, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Фотосессия')
        verbose_name_plural = ('Фотосессии')


class city(models.Model):
    title = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Локации-города')
        verbose_name_plural = ('Локации-города')


class boat(models.Model):
    title = models.CharField(max_length=30, db_index=True)
    city = models.ManyToManyField(city, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Яхта')
        verbose_name_plural = ('Список яхт')

class product(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Товар')
        verbose_name_plural = ('Список товаров')


class PhotoToolType(models.Model):
    title = models.CharField(max_length=30, verbose_name='Наименование')
    icon_type = models.CharField(max_length=30, blank=True, verbose_name='Иконка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Тип оборудования')
        verbose_name_plural = ('Тип оборудования')


class PhotoTool(models.Model):
    title = models.CharField(max_length=30, verbose_name='Наименование')
    serial_number = models.CharField(max_length=30, verbose_name='Серийный номер')
    extension_number = models.CharField(max_length=30, verbose_name='Внутрений номер')
    Photo_tool_type = models.ForeignKey(PhotoToolType, on_delete=models.CASCADE,verbose_name='Тип техники')
    owner = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name='Кому выдан')
    DateCreate = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    DateEdit = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.title
        return self.serial_number
        return self.extension_number
        return self.owner


    class Meta:
        verbose_name = ('Оборудование')
        verbose_name_plural = ('Оборудование')


class money_currency(models.Model):
    date_today = models.DateField(auto_now_add=True, editable=True, verbose_name='Дата')
    dollar = models.FloatField(max_length=5, verbose_name='Доллар')
    euro = models.FloatField(max_length=5, verbose_name='Евро')
    rubl = models.FloatField(max_length=5, verbose_name='Рубль')
    grivna = models.FloatField(max_length=5, verbose_name='Гривна')
    funts = models.FloatField(max_length=5, verbose_name='Фунты')

    class Meta:
        verbose_name = ('Курс валюты')
        verbose_name_plural = ('Курс валют')
