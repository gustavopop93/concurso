# Generated by Django 3.0.4 on 2020-05-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qamar', '0011_auto_20200527_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logospiedepagina',
            name='nombreLogo',
            field=models.CharField(max_length=25, verbose_name='Nombre de Logo'),
        ),
    ]
