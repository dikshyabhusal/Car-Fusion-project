from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")
    return HttpResponse(html)

def service(request):
    return render(request,"service.html")
    return HttpResponse(html)

def blog(request):
    return render(request,"blog.html")
    return HttpResponse(html)

def contact(request):
    return render(request,"contact.html")
    return HttpResponse(html)

def login(request):
    return render(request,"login.html")
    return HttpResponse(html)