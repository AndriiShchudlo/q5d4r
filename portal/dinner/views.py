# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import auth

from dinner.models import Food, Menu



def get_user(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'dinner/base.html', {"user": username})

def home(request):
    food = Food.objects.all()
    menu = Menu.objects.all()
    return render(request, 'dinner/home.html', {
        "foods": food,
        "menu": menu,
    })

def login(request):
    return render(request, 'dinner/login.html', {})

