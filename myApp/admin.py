from django.contrib import admin

# Register your models here.
from .models import Car,Order,Contact

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Contact)