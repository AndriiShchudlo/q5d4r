# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Menu(models.Model):
    sectionName = models.CharField(max_length=150)

    def __str__(self):
        return self.sectionName
