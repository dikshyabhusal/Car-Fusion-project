
from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Car, Order, Contact

def index(request):
	return render(request,'home.html')

def about(request):
    return render(request,'service.html ')

def register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        user_name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')
        user_password = request.POST.get('user_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if username already exists
        if User.objects.filter(username=user_name).exists():
            messages.error(request, "Username already taken")
            return redirect('register')
        
        # Check if email already exists
        if User.objects.filter(email=email_address).exists():
            messages.error(request, "Email already taken")
            return redirect('register')
        
        # Check if passwords match
        if user_password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Create a new user
        myuser = User.objects.create_user(username=user_name, email=email_address, password=user_password)
        myuser.first_name = full_name  # Store full_name in first_name field
        myuser.save()

        messages.success(request, "Your account has been successfully created!")
        return redirect('signin')
    
    else:
        return render(request, 'register.html')

def signin(request):
    if request.method == "POST":
        login_username = request.POST['loginusername']
        login_password = request.POST['loginpassword']

        user = authenticate(username = login_username,password = login_password)
        if user is not None:
            login(request, user)
            # messages.success(request,"Successfully logged in!")
            return redirect('vehicles')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signin')

    else:
        print("error")
        return render(request,'login.html')

def signout(request):
        logout(request)
        # messages.success(request,"Successfully logged out!")
        return redirect('home')
    
    # return HttpResponse('signout')

def vehicles(request):
    cars = Car.objects.all()
    # print(cars)
    params = {'car':cars}
    return render(request,'cars.html ',params)

def bill(request):
    cars = Car.objects.all()
    params = {'cars':cars}
    return render(request,'bill.html',params)

def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname','')
        billemail = request.POST.get('billemail','')
        billphone = request.POST.get('billphone','')
        billaddress = request.POST.get('billaddress','')
        billcity = request.POST.get('billcity','')
        cars11 = request.POST['cars11']
        dayss = request.POST.get('dayss','')
        date = request.POST.get('date','')
        fl = request.POST.get('fl','')
        tl = request.POST.get('tl','')
        # print(request.POST['cars11'])
        
        order = Order(name = billname,email = billemail,phone = billphone,address = billaddress,city=billcity,cars = cars11,days_for_rent = dayss,date = date,loc_from = fl,loc_to = tl)
        order.save()
        return redirect('home')
    else:
        print("error")
        return render(request,'bill.html')

def contact(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname','')
        contactemail = request.POST.get('contactemail','')
        contactnumber = request.POST.get('contactnumber','')
        contactmsg = request.POST.get('contactmsg','')

        contact = Contact(name = contactname, email = contactemail, phone_number = contactnumber,message = contactmsg)
        contact.save()
    return render(request,'contact.html ')
