# Generated by Django 4.2.2 on 2023-06-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categoria_detalles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comunicado',
            old_name='fecha_ultima_modificacion',
            new_name='fecha_modificacion',
        ),
    ]
