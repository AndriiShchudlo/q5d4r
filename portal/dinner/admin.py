# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Food, Menu, Purchase, Bascket, FoodDay
#
admin.site.register(FoodDay)
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Bascket)
admin.site.register(Purchase)
