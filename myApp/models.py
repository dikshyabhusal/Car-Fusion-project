
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

class Carmodel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="car/images",default="")

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    carmodel = models.ForeignKey(Carmodel, on_delete=models.CASCADE)
    car_id = models.IntegerField(default=0)
    car_name = models.CharField(max_length=30,default="")
    car_desc = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images",default="")
    stock = models.IntegerField(default=0)
    def __str__(self):
        return self.car_name

class Order(models.Model) :
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,default="")
    date_ordered = models.DateTimeField(auto_now_add=True)
    rental_duration = models.IntegerField()  # Rental duration in days
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default="")
    
    def __str__(self):
        return f"{self.user.username} ordered {self.car.name}"

class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    phone_number = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s wishlist"