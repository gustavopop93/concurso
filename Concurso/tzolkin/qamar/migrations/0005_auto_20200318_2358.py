# Generated by Django 3.0.4 on 2020-03-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qamar', '0004_auto_20200318_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='nombreActividad',
            field=models.CharField(max_length=200, verbose_name='Nombre de Actividad'),
        ),
        migrations.AlterField(
            model_name='tipoactividad',
            name='nombreTipoActividad',
            field=models.CharField(max_length=200, verbose_name='Tipo de Actividad'),
        ),
    ]