from django.db import models
from django.contrib.auth.models import User

class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, default="1317920625")
    telefono = models.CharField(max_length=20, default="0980643265")
    origen = models.CharField(max_length=100, default="Manta, EC")
    estado_civil = models.CharField(max_length=50, default="Soltero")

    class Meta:
        verbose_name_plural = "Datos Personales"

    def __str__(self):
        return self.nombre

class ExperienciaLaboral(models.Model):
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    funciones = models.TextField()

    class Meta:
        verbose_name_plural = "Experiencia Laboral"

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=100)
    progreso = models.IntegerField(default=100)

    def __str__(self):
        return self.titulo

class Reconocimiento(models.Model):
    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=100, default="Carrera en Curso")

    def __str__(self):
        return self.titulo

class ProyectoGarage(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Proyectos Garage Tech"

    def __str__(self):
        return self.nombre