from django.db import models

class Food(models.Model):
    id = models.IntegerField()
    food_name = models.CharField(max_length=256)
