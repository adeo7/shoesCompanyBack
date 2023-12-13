# Generated by Django 4.2.7 on 2023-12-02 07:09

import apps.pqrs.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0004_historicalusuariodatos_documento_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PqrInformacion',
            fields=[
                ('num_radicado', models.PositiveIntegerField(auto_created=True, unique=True, verbose_name='Número de Radicado')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha eliminacion')),
                ('tipo_peticion', models.TextField(max_length=50, null=True, unique=True, verbose_name='Tipo de peticion')),
                ('descripcion', models.TextField(max_length=255, null=True, unique=True, verbose_name='Descripcion peticion')),
                ('tiempo_restante', models.DateField(auto_now_add=True, verbose_name='Fecha de timepo restante')),
                ('fecha_estimada', models.DateField(default=apps.pqrs.models.PqrInformacion.get_fecha_estimada_default, verbose_name='Fecha de estimada')),
                ('archivos_pqrs', models.FileField(upload_to='pqrs/pqrs_informacion/')),
                ('local_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.localusuario', verbose_name='Local para la peticion')),
                ('usuariodatos_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuariodatos', verbose_name='Datos del usuario para la peticion')),
            ],
            options={
                'verbose_name': 'Pqr informacion',
                'verbose_name_plural': 'Pqrs informacion',
            },
        ),
        migrations.CreateModel(
            name='PqrRespuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha eliminacion')),
                ('descripcion', models.TextField(max_length=255, null=True, unique=True, verbose_name='Descripcion respuesta a peticion')),
                ('fecha_respuesta', models.DateField(auto_now=True, verbose_name='Fecha de respuesta')),
                ('archivos_respuesta_pqrs', models.FileField(upload_to='pqrs/pqrs_respuesta/')),
                ('pqr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pqrs.pqrinformacion', verbose_name='Pqr informacion de respuesta')),
            ],
            options={
                'verbose_name': 'Pqr respuesta',
                'verbose_name_plural': 'Pqrs respuest',
            },
        ),
        migrations.CreateModel(
            name='HistoricalPqrRespuesta',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha eliminacion')),
                ('descripcion', models.TextField(db_index=True, max_length=255, null=True, verbose_name='Descripcion respuesta a peticion')),
                ('fecha_respuesta', models.DateField(blank=True, editable=False, verbose_name='Fecha de respuesta')),
                ('archivos_respuesta_pqrs', models.TextField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('pqr_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pqrs.pqrinformacion', verbose_name='Pqr informacion de respuesta')),
            ],
            options={
                'verbose_name': 'historical Pqr respuesta',
                'verbose_name_plural': 'historical Pqrs respuest',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPqrInformacion',
            fields=[
                ('num_radicado', models.PositiveIntegerField(auto_created=True, db_index=True, verbose_name='Número de Radicado')),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha eliminacion')),
                ('tipo_peticion', models.TextField(db_index=True, max_length=50, null=True, verbose_name='Tipo de peticion')),
                ('descripcion', models.TextField(db_index=True, max_length=255, null=True, verbose_name='Descripcion peticion')),
                ('tiempo_restante', models.DateField(blank=True, editable=False, verbose_name='Fecha de timepo restante')),
                ('fecha_estimada', models.DateField(default=apps.pqrs.models.PqrInformacion.get_fecha_estimada_default, verbose_name='Fecha de estimada')),
                ('archivos_pqrs', models.TextField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('local_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='usuarios.localusuario', verbose_name='Local para la peticion')),
                ('usuariodatos_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='usuarios.usuariodatos', verbose_name='Datos del usuario para la peticion')),
            ],
            options={
                'verbose_name': 'historical Pqr informacion',
                'verbose_name_plural': 'historical Pqrs informacion',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]