# Generated by Django 3.1.4 on 2021-01-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_auto_20210111_0007'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_city',
            field=models.ManyToManyField(blank=True, default=None, to='photo.City'),
        ),
    ]
