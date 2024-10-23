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
    path('booking/', views.booking_form, name='booking_form'),
    path('pay-now/', views.pay_now, name='pay_now'),
    path('search/', views.search_cars, name='search_cars'),
    
    path('khalti-payment/', views.khalti_payment_verification, name='khalti_payment_verification'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),
    path('wishlist/add/<int:car_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/remove/<int:car_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    # path("vehicles",views.Order,name = 'vehicles'),
    # path("bike",views.bike,name = 'bike'),

    ]