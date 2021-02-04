# Generated by Django 3.1.4 on 2021-01-10 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20210111_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='city',
            field=models.ManyToManyField(blank=True, to='photo.City'),
        ),
        migrations.AlterField(
            model_name='photosessions',
            name='Client',
            field=models.ManyToManyField(blank=True, to='photo.Client'),
        ),
        migrations.AlterField(
            model_name='photosessions',
            name='boat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='photo.boat'),
        ),
        migrations.AlterField(
            model_name='photosessions',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='photo.city'),
        ),
    ]
