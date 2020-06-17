# Generated by Django 3.0.4 on 2020-05-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qamar', '0009_auto_20200527_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuatrimestre',
            name='nombreCuatrimestre',
            field=models.CharField(max_length=50, verbose_name='Cuatrimestre'),
        ),
        migrations.AlterField(
            model_name='epoca',
            name='nombreEpoca',
            field=models.CharField(max_length=50, verbose_name='Época'),
        ),
        migrations.AlterField(
            model_name='fase',
            name='nombreFase',
            field=models.CharField(max_length=50, verbose_name='Fase Lunar'),
        ),
        migrations.AlterField(
            model_name='logospiedepagina',
            name='nombreLogo',
            field=models.CharField(max_length=50, verbose_name='Nombre de Logo'),
        ),
        migrations.AlterField(
            model_name='tiempo',
            name='nombreTiempo',
            field=models.CharField(max_length=50, verbose_name='Tiempo'),
        ),
    ]
