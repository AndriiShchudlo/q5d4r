# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import auth

from dinner.models import Food, Menu
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
import logging

from django.template.context_processors import csrf


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

def basket(request):
    return render(request, 'dinner/basket.html', {})


def loginSys(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        inputUser = request.POST.get('inputUser', '')
        print inputUser
        inputPassword = request.POST.get('inputPassword', '')
        user = auth.authenticate(username = inputUser, password = inputPassword)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Користувач не знайдений"
            return render_to_response('dinner/login.html', args)
    else:
        return render_to_response('dinner/login.html', args)

def logout(request):
     auth.logout(request)
     return redirect('/')