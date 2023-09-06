from django.db import models
from datetime import datetime
# Create your models here.

class Carrossel(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=255)
    buttom = models.CharField(max_length=20)
    image = models.ImageField(upload_to='./images')

class Offer(models.Model):
    imagem = models.ImageField(upload_to="./images")

class Infor(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='./images')
    buttom = models.CharField(default= '', max_length=20)

class Depoi(models.Model):
    usuario = models.CharField(max_length=40)
    description = models.TextField(max_length=255)
    perfil = models.ImageField(upload_to="./images")
    data = models.DateField(default= datetime.now, blank= True)

class Products(models.Model):
    imagem = models.ImageField(upload_to='./images')
    title = models.CharField(default="", max_length=20)
    preco = models.DecimalField(default=000.00, max_digits=5, decimal_places=2 )
    description = models.TextField(max_length=200)