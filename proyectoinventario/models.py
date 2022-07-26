from tabnanny import verbose
from django.db import models

# Create your models here.

class Assets(models.Model):
    
    modelo=models.CharField(max_length=30)
    serie=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    cantidad=models.CharField(max_length=3)
    tipo=models.CharField(max_length=10)
    categoria=models.CharField(max_length=10)
    estado=models.CharField(max_length=10)
    fecha=models.DateTimeField(auto_now_add=True)
    accion=models.CharField(max_length=10)

    