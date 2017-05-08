# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
from django.db import models

# # Create your models here.
# #
class FoodDay(models.Model):
    class Meta:
        db_table = "food_day"
    foodDay = models.TextField()
    foodDayNumber = models.IntegerField(default=1)
    def __str__(self):
        return self.foodDay


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
    foodDay = models.ForeignKey(FoodDay)

    def __str__(self):
        return self.foodName


class Bascket(models.Model):
    class Meta:
        db_table = "bascket"
    productName = models.TextField()
    productCategory = models.TextField()
    productPrice = models.FloatField()
    def __str__(self):
        return self.productName

class Purchase(models.Model):
    class Meta:
        db_table = "purchase"
    username = models.TextField()
    purchaseId = models.ForeignKey(Bascket)
