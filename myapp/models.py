from django.db import models

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)