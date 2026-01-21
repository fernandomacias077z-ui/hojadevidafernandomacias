from django.contrib import admin
from .models import Task

# Registramos solo el modelo Task para que el admin de Django funcione
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

admin.site.register(Task, TaskAdmin)