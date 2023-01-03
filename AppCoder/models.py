from django.db import models
from datetime import datetime as dt
# Create your models here.
class Pago(models.Model):
    tipo_tarjeta=models.CharField(max_length=40)
    cuotas=models.IntegerField()

class Productos(models.Model):
    categoria=models.CharField(max_length=40)
    rango_precio=models.IntegerField()
    
class Vendedores(models.Model):
    localidad=models.CharField(max_length=40)
    tiempo_de_entrega=models.IntegerField()
    calificacion=models.IntegerField()
