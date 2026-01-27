from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, default="Bruno Fernando Macias Moreira") #
    email = models.EmailField(default="Franyo678@gmail.com") #
    phone = models.CharField(max_length=20, default="0980643265") #
    location = models.CharField(max_length=200, default="Jocay j4 y j9, Manta, Ecuador") #
    summary = models.TextField(default="Profesional de sala con experiencia en restaurantes...") #

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    description = models.TextField()