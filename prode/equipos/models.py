from django.db import models

class Equipos(models.Model):
    nombre = models.CharField(max_length=255)
