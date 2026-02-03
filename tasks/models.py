from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    origen = models.CharField(max_length=200)
    estado_civil = models.CharField(max_length=50, default="Soltero")

    class Meta:
        verbose_name_plural = "Datos Personales"

    def __str__(self):
        return self.nombre

class ExperienciaLaboral(models.Model):
    puesto = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    actualidad = models.BooleanField(default=False)
    funciones = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Experiencias Laborales"

    def clean(self):
        super().clean()
        if self.fecha_fin and self.fecha_inicio and self.fecha_fin < self.fecha_inicio:
            raise ValidationError({'fecha_fin': _('La fecha de fin no puede ser anterior a la de inicio.')})
        if self.actualidad and self.fecha_fin:
            raise ValidationError({'fecha_fin': _('Si es un trabajo actual, no debe tener fecha de fin.')})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.puesto} - {self.empresa}"

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    certificado_pdf = models.FileField(upload_to='certificados/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class ProyectoGarage(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField(default=100)

    class Meta:
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.nombre

class Reconocimiento(models.Model):
    nombre = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    en_curso = models.BooleanField(default=False, verbose_name="¿Está en curso?")
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Reconocimientos"

    def clean(self):
        super().clean()
        if self.fecha_fin and self.fecha_inicio and self.fecha_fin < self.fecha_inicio:
            raise ValidationError({'fecha_fin': _('La fecha de fin no puede ser anterior a la de inicio.')})
        if self.en_curso and self.fecha_fin:
            raise ValidationError({'fecha_fin': _('Si el reconocimiento está en curso, no debe tener fecha de fin.')})
        if not self.en_curso and not self.fecha_fin:
            raise ValidationError({'fecha_fin': _('Debe indicar una fecha de fin si el reconocimiento ya fue terminado.')})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        estado = " (En curso)" if self.en_curso else ""
        return f"{self.nombre}{estado}"