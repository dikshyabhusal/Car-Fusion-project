
from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import Car, Order, Contact,Carmodel,Order,Wishlist
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.conf import settings


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

def admin_add_carmodel_validation(request):
    if request.method == "POST":
        carmodel_name = request.POST['c_name']  # Make sure this matches your form field name
        carmodel_image = request.FILES['c_image']
        
        # Create the Carmodel using the correct field name
        Car_models.objects.create(name=carmodel_name, image=carmodel_image)  # Use 'name' if that's the field name
        
        messages.success(request, "Car model added successfully")
        return redirect('admin_add_carmodel')


def booking_form(request):
    if request.method == 'POST':
        # Handle form submission and redirect to the pay now page
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        car = request.POST['car']
        days_for_rent = request.POST['days_for_rent']
        pickup_date = request.POST['pickup_date']
        
        # You can pass this data to the payment page
        request.session['booking_details'] = {
            'name': name,
            'email': email,
            'phone': phone,
            'car': car,
            'days_for_rent': days_for_rent,
            'pickup_date': pickup_date
        }
        return redirect('pay_now')

    return render(request, 'bill.html')

def pay_now(request):
    booking_details = request.session.get('booking_details')
    return render(request, 'payment.html', {'booking_details': booking_details})

@csrf_exempt
def khalti_payment_verification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token')
        amount = data.get('amount')

        headers = {
            "Authorization": f"Key {settings.KHALTI_SECRET_KEY}"
        }
        payload = {
            "token": token,
            "amount": amount
        }
        
        # Send request to Khalti's verify endpoint
        response = requests.post('https://khalti.com/api/v2/payment/verify/', headers=headers, data=payload)
        response_data = response.json()

        if response.status_code == 200 and response_data.get('state') == 'Completed':
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': response_data})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')

@login_required
def add_to_wishlist(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    # Get the currently logged-in user
    user = request.user

    # Ensure user is authenticated before adding to wishlist
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated

    # Create a new Wishlist entry, or get the existing one
    wishlist, created = Wishlist.objects.get_or_create(user=user, car=car)

    # Redirect to a success page or wishlist page
    return redirect('wishlist_view')

# Display wishlist
@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

# Remove car from wishlist
@login_required
def remove_from_wishlist(request, car_id):
    car = Car.objects.get(id=car_id)
    Wishlist.objects.filter(user=request.user, car=car).delete()
    return redirect('wishlist')

def search_cars(request):
    query = request.GET.get('query', '')
    search_results = Car.objects.filter(name__icontains=query)  # Change 'name' to the relevant field in your Car model
    context = {
        'search_results': search_results,
        'query': query
    }
    return render(request, 'search_results.html', context)

