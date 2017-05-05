from django.conf.urls import url
from . import views

from . import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^home/', views.home, name="home"),
    url(r'^basket/', views.basket, name="bascket"),
]
