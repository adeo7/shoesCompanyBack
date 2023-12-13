# Generated by Django 4.2.7 on 2023-12-06 07:31

import apps.pqrs.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pqrs', '0006_remove_historicalpqrrespuesta_usuariodatos_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpqrinformacion',
            name='archivos_pqrs',
        ),
        migrations.RemoveField(
            model_name='historicalpqrrespuesta',
            name='archivos_respuesta_pqrs',
        ),
        migrations.RemoveField(
            model_name='pqrinformacion',
            name='archivos_pqrs',
        ),
        migrations.RemoveField(
            model_name='pqrrespuesta',
            name='archivos_respuesta_pqrs',
        ),
        migrations.CreateModel(
            name='HistoricalArchivosPqrRespuesta',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha eliminacion')),
                ('codigo', models.TextField(max_length=10, verbose_name='Codigo de archivo')),
                ('archivos_respuesta_pqrs', models.TextField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('pqr_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pqrs.pqrrespuesta', verbose_name='Pqr respuesta')),
                ('pqr_info_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pqrs.pqrinformacion', verbose_name='Pqr informacion de respuesta')),
            ],
            options={
                'verbose_name': 'historical Archivo de respuesta de Pqr',
                'verbose_name_plural': 'historical Archivos de respuesta de Pqrs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalArchivosPqrInformacion',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha eliminacion')),
                ('codigo', models.TextField(max_length=10, verbose_name='Codigo de archivo')),
                ('archivos_pqrs', models.TextField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('pqr_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pqrs.pqrinformacion', verbose_name='Pqr informacion')),
            ],
            options={
                'verbose_name': 'historical Archivo de Pqr',
                'verbose_name_plural': 'historical Archivos de Pqrs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='ArchivosPqrRespuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha eliminacion')),
                ('codigo', models.TextField(max_length=10, verbose_name='Codigo de archivo')),
                ('archivos_respuesta_pqrs', models.FileField(upload_to=apps.pqrs.models.ArchivosPqrRespuesta.upload_to_respuesta_pqrs)),
                ('pqr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pqrs.pqrrespuesta', verbose_name='Pqr respuesta')),
                ('pqr_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pqrs.pqrinformacion', verbose_name='Pqr informacion de respuesta')),
            ],
            options={
                'verbose_name': 'Archivo de respuesta de Pqr',
                'verbose_name_plural': 'Archivos de respuesta de Pqrs',
            },
        ),
        migrations.CreateModel(
            name='ArchivosPqrInformacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha eliminacion')),
                ('codigo', models.TextField(max_length=10, verbose_name='Codigo de archivo')),
                ('archivos_pqrs', models.FileField(upload_to=apps.pqrs.models.ArchivosPqrInformacion.upload_to_pqrs)),
                ('pqr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pqrs.pqrinformacion', verbose_name='Pqr informacion')),
            ],
            options={
                'verbose_name': 'Archivo de Pqr',
                'verbose_name_plural': 'Archivos de Pqrs',
            },
        ),
    ]
