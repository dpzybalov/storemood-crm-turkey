# Generated by Django 3.1.4 on 2021-01-10 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20210110_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoSessionsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='money_currency',
            new_name='MoneyCurrency',
        ),
        migrations.RemoveField(
            model_name='photosessions',
            name='client',
        ),
        migrations.RemoveField(
            model_name='photosessions',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='phototool',
            name='state',
        ),
        migrations.AddField(
            model_name='photosessions',
            name='Client',
            field=models.ManyToManyField(blank=True, to='photo.Client'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='city',
            field=models.ManyToManyField(blank=True, to='photo.City'),
        ),
        migrations.DeleteModel(
            name='PhotoToolState',
        ),
        migrations.AddField(
            model_name='photosessionsimage',
            name='Photosessions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photo.photosessions'),
        ),
    ]