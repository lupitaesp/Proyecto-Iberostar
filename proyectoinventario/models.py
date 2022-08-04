from tabnanny import verbose
from django.db import models

# Create your models here.

class Assets(models.Model):
    id = models.AutoField(primary_key=True)
    modelo=models.CharField(max_length=30)
    serie=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    cantidad=models.CharField(max_length=3)
    tipo=models.CharField(max_length=10)
    categoria=models.CharField(max_length=10)
    estado=models.CharField(max_length=10)
    fecha=models.DateTimeField(auto_now_add=True)
    año_compra=models.CharField(max_length=4)
    accion=models.CharField(max_length=10)

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=60)
    email=models.EmailField()
    departamento=models.CharField(max_length=50)
    hotel=models.CharField(max_length=50)
    upated=models.DateTimeField(auto_now_add=True)
    descripcion=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    