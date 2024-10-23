from django.contrib import admin

# Register your models here.
from .models import Car,Order,Contact,User,Carmodel,Wishlist

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Carmodel)
admin.site.register(Wishlist)