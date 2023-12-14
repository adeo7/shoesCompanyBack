from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
from apps.usuarios.models import LocalUsuario, Usuario
from datetime import timedelta
from django.utils import timezone
import random

class PqrInformacion(BaseModel):
    def get_fecha_estimada_default():
        # Retorna la fecha actual más 14 días
        return timezone.now() + timedelta(days=14)

    peticion = models.CharField('Tipo peticion', max_length=30, blank=False, null=True)
    num_radicado = models.PositiveIntegerField('Número de Radicado', unique=True, null=True, blank=True)
    descripcion = models.TextField('Descripcion peticion', max_length=255, blank=False, null=True, unique=True)
    tiempo_restante = models.DateField('Fecha de timepo restante', auto_now=False, auto_now_add=True)
    fecha_estimada = models.DateField('Fecha de estimada', default=get_fecha_estimada_default)
    local_id = models.ForeignKey(LocalUsuario, on_delete=models.CASCADE, verbose_name='Local para la peticion', null=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario', null=True)
    historical = HistoricalRecords(inherit=True)

    def save(self, *args, **kwargs):
        if not self.num_radicado:
            max_value = 999999  # El valor máximo del número aleatorio (ajústalo según tu preferencia)
            while True:
                num = random.randint(1, max_value)
                # Verifica si el número generado ya existe en la base de datos
                if not PqrInformacion.objects.filter(num_radicado=num).exists():
                    self.num_radicado = num
                    break
        super().save(*args, **kwargs)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return str(self.num_radicado)

    class Meta:
        verbose_name = 'Pqr informacion'
        verbose_name_plural = 'Pqrs informacion'

class PqrRespuesta(BaseModel):

    descripcion = models.TextField('Descripcion respuesta a peticion', max_length=255, blank=False, null=True, unique=True)
    fecha_respuesta = models.DateField('Fecha de respuesta', auto_now=True, auto_now_add=False)
    local_id = models.ForeignKey(LocalUsuario, on_delete=models.CASCADE, verbose_name='Local para la respuesta', null=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario', null=True)
    pqr_id = models.ForeignKey(PqrInformacion, on_delete=models.CASCADE, verbose_name='Pqr informacion de respuesta')
    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Pqr respuesta'
        verbose_name_plural = 'Pqrs respuesta'

class ArchivosPqrInformacion(BaseModel):
    def upload_to_pqrs(instance, filename):
        return f"pqrs/pqrs_informacion/{instance.pqr_id}/{filename}"

    codigo = models.PositiveIntegerField('Codigo', unique=True)
    archivos_pqrs = models.FileField(upload_to=upload_to_pqrs)
    pqr_id = models.ForeignKey(PqrInformacion, on_delete=models.CASCADE, verbose_name='Pqr informacion')
    historical = HistoricalRecords(inherit=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            max_value = 999999  # El valor máximo del número aleatorio (ajústalo según tu preferencia)
            while True:
                num = random.randint(1, max_value)
                # Verifica si el número generado ya existe en la base de datos
                if not ArchivosPqrInformacion.objects.filter(codigo=num).exists():
                    self.num_radicado = num
                    break
        super().save(*args, **kwargs)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Archivo de Pqr'
        verbose_name_plural = 'Archivos de Pqrs'

class ArchivosPqrRespuesta(BaseModel):
    def upload_to_respuesta_pqrs(instance, filename):
        return f"pqrs/pqrs_respuesta/{instance.pqr_id}/{filename}"

    codigo = models.PositiveIntegerField('Codigo', unique=True)
    archivos_respuesta_pqrs = models.FileField(upload_to=upload_to_respuesta_pqrs)
    pqr_id = models.ForeignKey(PqrRespuesta, on_delete=models.CASCADE, verbose_name='Pqr respuesta')
    pqr_info_id = models.ForeignKey(PqrInformacion, on_delete=models.CASCADE, verbose_name='Pqr informacion de respuesta')
    historical = HistoricalRecords(inherit=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            max_value = 999999  # El valor máximo del número aleatorio (ajústalo según tu preferencia)
            while True:
                num = random.randint(1, max_value)
                # Verifica si el número generado ya existe en la base de datos
                if not ArchivosPqrInformacion.objects.filter(codigo=num).exists():
                    self.num_radicado = num
                    break
        super().save(*args, **kwargs)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Archivo de respuesta de Pqr'
        verbose_name_plural = 'Archivos de respuesta de Pqrs'
