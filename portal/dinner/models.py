# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class NewMenu(models.Model):
    section = models.TextField()
    sectionImage = models.TextField()

    def __str__(self):
        return self.section
class Item(models.Model):
     name = models.TextField()
     sectionid = models.TextField()