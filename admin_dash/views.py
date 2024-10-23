from django.shortcuts import render, redirect
from myApp.models import Car, Carmodel  # Ensure correct model names
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Views

@login_required(login_url='/admin/admin_login/')
def admin_home(request):
    return render(request, "admin_panel/index.html")

@login_required(login_url='/admin/admin_login/')
def admin_car(request):
    all_carmodels = Carmodel.objects.all()  # Use correct model name
    all_cars = Car.objects.all()
    data = {
        "categories": all_carmodels,
        "cars": all_cars,
        "active_page": 'car'
    }
    return render(request, "admin_panel/cars.html", data)

def admin_add_carmodel(request):
    return render(request, "admin_panel/add_carmodels.html")

def admin_add_carmodel_validation(request):
    carmodel_name = request.POST['c_name']
    carmodel_image = request.FILES['c_image']
    Carmodel.objects.create(name=carmodel_name, image=carmodel_image)  # Updated field names
    messages.success(request, "Carmodel added Successfully")
    return redirect('admin_add_carmodel')

@login_required(login_url='admin_login')
def add_car(request):
    Carmodel_list = Carmodel.objects.all()
    return render(request, "admin_panel/add_car.html", {"show_Carmodel": Carmodel_list})

def admin_add_car_validation(request):
    if request.POST:
        car_name = request.POST['p_name']
        car_price = request.POST['p_price']
        car_discount = request.POST['p_discount']
        car_image = request.FILES['p_image']
        car_description = request.POST['p_description']
        car_Carmodel = request.POST['p_carmodel']
        car_stock = request.POST['p_stock']
        Car.objects.create(
            name=car_name,
            price=car_price,
            discount=car_discount,
            image=car_image,
            description=car_description,
            carmodels_id=car_Carmodel,  # Correct field name
            stock=car_stock
        )
        messages.success(request, "Car added Successfully")
        return redirect("add_car")

@login_required(login_url='admin_login')
def admin_account(request):
    if request.method == "POST":
        print("Login POST data:", request.POST)
    return render(request, "admin_panel/accounts.html")

@csrf_exempt
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/admin/admin_car/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('admin_login')
    else:
        return render(request, "admin_panel/login.html")

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def delete_selected_cars(request):
    if request.method == 'POST':
        car_ids = request.POST.getlist('selected_cars')
        if car_ids:
            Car.objects.filter(id__in=car_ids).delete()  # Correct class name
            messages.success(request, "Selected cars deleted successfully")
        else:
            messages.error(request, "No cars selected for deletion")
    return redirect('admin_car')
