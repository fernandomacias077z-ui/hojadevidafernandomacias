from django.db import models
from django.core.exceptions import ValidationError

class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, verbose_name="Cédula/DNI", null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    sector = models.CharField(max_length=100, verbose_name="Barrio/Sector", null=True, blank=True)
    resumen = models.TextField()
    foto = models.ImageField(upload_to='perfil/', null=True, blank=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil (Información Personal)"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Experiencia(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='experiencias', null=True, blank=True)
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to='experiencia/logos/', null=True, blank=True)
    archivo = models.FileField(upload_to='experiencia/archivos/', null=True, blank=True)

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencia Laboral"

class Educacion(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='educacion', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(null=True, blank=True)
    logo = models.ImageField(upload_to='educacion/logos/', null=True, blank=True)
    archivo = models.FileField(upload_to='educacion/archivos/', null=True, blank=True)

    class Meta:
        verbose_name = "Producto Académico"
        verbose_name_plural = "Productos Académicos"

class Proyecto(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='proyectos', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField()
    fecha = models.DateField(null=True, blank=True)
    tecnologias = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    logo = models.ImageField(upload_to='proyectos/logos/', null=True, blank=True)
    archivo = models.FileField(upload_to='proyectos/archivos/', null=True, blank=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos (Portafolio)"

# --- MODELO QUE FALTABA Y CAUSABA EL ERROR ---
class Certificado(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='certificados', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha = models.DateField(blank=True, null=True)
    archivo = models.FileField(upload_to='certificados/', blank=True, null=True)

    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

    def __str__(self):
        return self.titulo

class Producto(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos_venta', null=True, blank=True)
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default='Buen Estado')
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    class Meta:
        verbose_name = "Producto de Venta"
        verbose_name_plural = "Garage (Ventas)"

class Curso(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='cursos', null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    pdf_archivo = models.FileField(upload_to='cursos/pdfs/')
    vista_previa = models.ImageField(upload_to='cursos/previews/', null=True, blank=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"