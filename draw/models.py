from django.db import models

# Create your models here.
class Canvas(models.Model):
    img = models.ImageField()
