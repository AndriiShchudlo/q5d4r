# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
from django.db import models

# # Create your models here.
# #
class FirstFood(models.Model):
    class Meta:
        db_table = "first_food"
    firstFoodName = models.TextField()
    firstFoodPrice = models.FloatField()
    firstFoodImage = models.TextField(default=None)
    def __str__(self):
        return self.firstFoodName

#
class SecondFood(models.Model):
    class Meta:
        db_table = "second_food"
    secondFoodName = models.TextField()
    secondFoodPrice = models.FloatField()
    secondFoodImage = models.TextField(default=None)
    def __str__(self):
        return self.secondFoodName