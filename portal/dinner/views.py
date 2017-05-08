# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.functions import datetime
from django.shortcuts import render
from django.contrib import auth

from dinner.models import Food, Menu
from django.shortcuts import render_to_response, redirect
from django.contrib import auth

from django.template.context_processors import csrf
from workWithDate import Date

def get_user(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'dinner/base.html', {"user": username})



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
        user = auth.authenticate(username=inputUser, password = inputPassword)
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

def dinnerMenu(request):
    food = Food.objects.all()
    menu = Menu.objects.all()
    foodDay = request.POST.get('dinnerDate', '')
    print (foodDay+"da")
    datas = {
        "foods": food,
        "menu": menu,
    }
    return render(request,'dinner/dinnerMenu.html', datas)

def home(request):

    return render(request, 'dinner/home.html', {})