from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Inventories(models.Model):
    sku = models.CharField(max_length=8)
    inventario = models.SmallIntegerField(default=100, validators=[MaxValueValidator(100000), MinValueValidator(100)])
    umbral = models.SmallIntegerField(default=10, validators=[MinValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
    sku = models.CharField(max_length=8)
    cantidad = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

