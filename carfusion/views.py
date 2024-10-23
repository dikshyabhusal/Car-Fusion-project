from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"home.html")
    return HttpResponse(html)

def service(request):
    return render(request,"service.html")
    return HttpResponse(html)

def Our_Cars(request):
    return render(request,"cars.html")
    return HttpResponse(html)

def contact(request):
    return render(request,"contact.html")
    return HttpResponse(html)

def login(request):
    return render(request,"login.html")
    return HttpResponse(html)

