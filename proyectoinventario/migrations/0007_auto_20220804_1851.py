# Generated by Django 2.2.3 on 2022-08-04 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoinventario', '0006_auto_20220804_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='año_compra',
            new_name='fecha_compra',
        ),
        migrations.RenameField(
            model_name='assets',
            old_name='id',
            new_name='id_asset',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='id',
            new_name='id_clientes',
        ),
    ]
