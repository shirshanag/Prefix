from django.shortcuts import render
from django.http import HttpResponse
from .models import user_data
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def pricing(request):
    return render(request,'pricing.html')
def services(request):
    return render(request,'services.html')
def shop(request):
    return render(request,'shop.html')
def login(request):
    if request.method=='POST':
        a1=request.POST['name']
        a2=request.POST['email']
        a3=request.POST['contact']
        a4=request.POST['password']
        data=user_data(name=a1,email=a2,contact=a3,password=a4)
        data.save()
    return render(request,'login.html')