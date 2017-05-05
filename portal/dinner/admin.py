# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Food, Menu, Purchase, Bascket
#
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(Bascket)
admin.site.register(Purchase)
