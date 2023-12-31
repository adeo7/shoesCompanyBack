# Generated by Django 4.2.7 on 2023-12-14 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0011_remove_historicalpqrinformacion_peticion_pqr_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivospqrinformacion',
            name='codigo',
            field=models.PositiveIntegerField(unique=True, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='archivospqrrespuesta',
            name='codigo',
            field=models.PositiveIntegerField(unique=True, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='historicalarchivospqrinformacion',
            name='codigo',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='historicalarchivospqrrespuesta',
            name='codigo',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Codigo'),
        ),
    ]
