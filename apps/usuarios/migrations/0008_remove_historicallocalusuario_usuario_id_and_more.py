# Generated by Django 4.2.7 on 2023-12-04 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_remove_historicalusuario_locales_usuarios_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicallocalusuario',
            name='usuario_id',
        ),
        migrations.RemoveField(
            model_name='localusuario',
            name='usuario_id',
        ),
        migrations.AddField(
            model_name='historicalusuario',
            name='locales_usuarios',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='usuarios.localusuario', verbose_name='Local para usuario'),
        ),
        migrations.AddField(
            model_name='historicalusuariodatos',
            name='documento',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='locales_usuarios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.localusuario', verbose_name='Local para usuario'),
        ),
        migrations.AddField(
            model_name='usuariodatos',
            name='documento',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='historicallocalusuario',
            name='direccion_local',
            field=models.CharField(max_length=50, verbose_name='Direccion local'),
        ),
        migrations.AlterField(
            model_name='historicallocalusuario',
            name='nit_local',
            field=models.CharField(max_length=9, verbose_name='Nit local'),
        ),
        migrations.AlterField(
            model_name='historicallocalusuario',
            name='nombre_local',
            field=models.CharField(max_length=40, verbose_name='Nombre local'),
        ),
        migrations.AlterField(
            model_name='historicallocalusuario',
            name='telefono_local',
            field=models.CharField(max_length=10, verbose_name='Telefono local'),
        ),
        migrations.AlterField(
            model_name='localusuario',
            name='direccion_local',
            field=models.CharField(max_length=50, verbose_name='Direccion local'),
        ),
        migrations.AlterField(
            model_name='localusuario',
            name='nit_local',
            field=models.CharField(max_length=9, verbose_name='Nit local'),
        ),
        migrations.AlterField(
            model_name='localusuario',
            name='nombre_local',
            field=models.CharField(max_length=40, verbose_name='Nombre local'),
        ),
        migrations.AlterField(
            model_name='localusuario',
            name='telefono_local',
            field=models.CharField(max_length=10, verbose_name='Telefono local'),
        ),
    ]