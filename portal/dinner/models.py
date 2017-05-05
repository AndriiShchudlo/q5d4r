# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
from django.db import models

# # Create your models here.
# #


class Menu(models.Model):
    class Meta:
        db_table = "menu"
    categoryName = models.TextField()
    categoryPrice = models.FloatField()
    def __str__(self):
        return self.categoryName

class Food(models.Model):
    class Meta:
        db_table = "food"
    foodName = models.TextField()
    foodImage = models.TextField(default=None)
    foodCategory = models.ForeignKey(Menu)

    def __str__(self):
        return self.foodName
