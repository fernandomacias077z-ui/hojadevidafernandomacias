from django.db import models
from django.contrib.auth.models import User

# --- PERFIL DE USUARIO ---
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, default="Bruno Fernando Macias Moreira")
    email = models.EmailField(default="Franyo678@gmail.com")
    phone = models.CharField(max_length=20, default="0980643265")
    location = models.CharField(max_length=200, default="Jocay j4 y j9, Manta, Ecuador")
    summary = models.TextField(default="Profesional de sala con experiencia en restaurantes...")

# --- MODELOS PARA TU CV ---
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
    periodo = models.CharField(max_length=100, help_text="Ej: Ene 2026 - Actualidad")
    funciones = models.TextField()
    estado = models.CharField(
        max_length=20, 
        choices=[('En curso', 'En curso'), ('Finalizado', 'Finalizado')], 
        default='Finalizado'
    )

    class Meta:
        verbose_name_plural = "Experiencia Laboral"

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.nombre

# --- OTROS ---
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title