# Generated by Django 3.1.4 on 2021-01-06 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('gorod', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='money_currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_today', models.DateField(auto_now_add=True)),
                ('dollar', models.FloatField(max_length=5)),
                ('euro', models.FloatField(max_length=5)),
                ('rubl', models.FloatField(max_length=5)),
                ('grivna', models.FloatField(max_length=5)),
                ('funts', models.FloatField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoToolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('icon_type', models.CharField(blank=True, max_length=30, verbose_name='Иконка')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Наименование')),
                ('serial_number', models.CharField(max_length=30, verbose_name='Серийный номер')),
                ('extension_number', models.CharField(max_length=30, verbose_name='Внутрений номер')),
                ('DateCreate', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('DateEdit', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('Photo_tool_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.phototooltype', verbose_name='Тип техники')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Кому выдан')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoSessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('user', models.CharField(blank=True, max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('photos', models.FileField(blank=True, upload_to='photos/%d/%m/%Y/')),
                ('status', models.CharField(default='Новая', max_length=30)),
                ('created_at', models.DateField(auto_now=True)),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='photo.boat')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='photo.city')),
                ('client', models.ManyToManyField(blank=True, to='photo.client')),
            ],
        ),
        migrations.AddField(
            model_name='boat',
            name='city',
            field=models.ManyToManyField(blank=True, to='photo.city'),
        ),
    ]
