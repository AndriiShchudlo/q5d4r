# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render



from dinner.models import NewMenu

from dinner.models import Item


def home(request):
    menuSection = NewMenu.objects.all()
    item = Item.objects.all()
    return render(request, 'dinner/home.html', {
        "menus": menuSection,
        "items": item
    })
