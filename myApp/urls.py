from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("home",views.index, name = 'home'),
    path("about",views.about,name = 'about'),
    path("vehicles", views.vehicles, name= "vehicles"),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout",views.signout,name = "signout"),
    path("bill",views.order,name = "bill"),
    path("contact",views.contact,name = 'contact'),
    # path("vehicles",views.Order,name = 'vehicles'),
    # path("bike",views.bike,name = 'bike'),

    ]