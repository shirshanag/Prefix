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
def signup(request):
    if request.method=='POST':
        a1=request.POST['name']
        a2=request.POST['email']
        a3=request.POST['contact']
        a4=request.POST['password']
        a5=request.POST['confirm_password']
        if a4!=a5:
            return HttpResponse("Password an confirm password must be same")
        if a1=="":
            return HttpResponse("Name is an Important field")
        if len(a4)<8:
            return HttpResponse("Password must be atmost 8 character")
        data=user_data(name=a1,email=a2,contact=a3,password=a4)
        data.save()
    return render(request,'signup.html')