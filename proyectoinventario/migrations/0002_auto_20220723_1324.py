# Generated by Django 2.2.3 on 2022-07-23 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoinventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dispositivos',
            new_name='Assets',
        ),
        migrations.AlterModelOptions(
            name='assets',
            options={},
        ),
    ]
