# Generated by Django 4.2.7 on 2023-12-13 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_alter_historicallocalusuario_usuario_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecuperarContraseña',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='Fecha eliminacion')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalRecuperarContraseña',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_at', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('deleted_at', models.DateField(blank=True, editable=False, verbose_name='Fecha eliminacion')),
                ('token', models.CharField(db_index=True, max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'verbose_name_plural': 'historical Modelos Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
