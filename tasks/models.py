from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# MODELO ACTUALIZADO SEGÚN TU SQL
class DatosPersonales(models.Model):
    SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino')]
    
    idperfil = models.IntegerField(primary_key=True, verbose_name="ID Perfil")
    descripcionperfil = models.CharField(max_length=50, blank=True, null=True)
    perfilactivo = models.IntegerField(default=1)
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField()
    numerocedula = models.CharField(max_length=10)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estadocivil = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=6, blank=True, null=True)
    telefonoconvencional = models.CharField(max_length=15, blank=True, null=True)
    telefonofijo = models.CharField(max_length=15, blank=True, null=True)
    direcciontrabajo = models.CharField(max_length=50, blank=True, null=True)
    direcciondomiciliaria = models.CharField(max_length=50)
    sitioweb = models.CharField(max_length=60, blank=True, null=True)

    @property
    def nombre(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name_plural = "Datos Personales"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

# RECOBRANDO LOS MODELOS QUE FALTABAN (Importante para tus vistas)
class ExperienciaLaboral(models.Model):
    puesto = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    actualidad = models.BooleanField(default=False)
    funciones = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Experiencias Laborales"

    def __str__(self):
        return f"{self.puesto} - {self.empresa}"

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    certificado_pdf = models.FileField(upload_to='certificados/', null=True, blank=True)

    def __str__(self):
        return self.nombre

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
    en_curso = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Reconocimientos"

    def __str__(self):
        return self.nombre

class ProyectoGarage(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo