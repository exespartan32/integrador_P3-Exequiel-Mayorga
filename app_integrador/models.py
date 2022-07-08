from django.db import models
# Create your models here.
class Diario(models.Model):
    titulo = models.CharField(max_length=200)
    epigrafe = models.TextField()
    cuerpo = models.TextField()