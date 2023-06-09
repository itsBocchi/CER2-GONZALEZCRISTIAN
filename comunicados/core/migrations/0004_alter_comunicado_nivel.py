# Generated by Django 4.2.2 on 2023-06-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_fecha_ultima_modificacion_comunicado_fecha_modificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='nivel',
            field=models.CharField(choices=[('GEN', 'General'), ('PRE', 'Preescolar'), ('BAS', 'Básico'), ('MED', 'Medio')], max_length=20),
        ),
    ]