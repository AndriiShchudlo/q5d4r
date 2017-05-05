# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import auth


from dinner.models import FirstFood, SecondFood


def home(request):
    firstFoods = FirstFood.objects.all()
    secondFoods = SecondFood.objects.all()
    return render(request, 'dinner/home.html', {
        "firstFoods": firstFoods,
        "secondFoods": secondFoods,
    })

def login(request):
    return render(request, 'dinner/login.html', {})