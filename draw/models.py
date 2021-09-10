from django.db import models

# Create your models here.
class DrawingTools(models.Model):
    order = models.IntegerField()
    tool = models.CharField(max_length=80)


class Canvas(models.Model):
    img = models.ImageField()
    last_tool = models.ForeignKey(DrawingTools, on_delete=models.CASCADE, null=True)
