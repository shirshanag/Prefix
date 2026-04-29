from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_data
from .models import contact_data
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        u1=request.POST['Your_Name']
        u2=request.POST['Email']
        u3=request.POST['Message']
        con_data=contact_data(Your_Name=u1,Email=u2,Message=u3)
        con_data.save()
    return render(request,'contact.html')
def pricing(request):
    return render(request,'pricing.html')
def services(request):
    return render(request,'services.html')
@login_required(login_url='login')

def shop(request):
    if 'user' not in request.session:
        return redirect('login')
    products=Product.objects.all()
    return render(request,'shop.html',{"products":products})
def signup(request):
    if request.method=='POST':
        a1=request.POST['name']
        a2=request.POST['email']
        a3=request.POST['contact']
        a4=request.POST['password']
        a5=request.POST['confirm_password']
        if a1 == "":
            return render(request, 'signup.html', {'error': 'Name is a required field'})
        if a4 != a5:
            return render(request, 'signup.html', {'error': 'Password and confirm password must be same'})
        if len(a4) < 8:
            return render(request, 'signup.html', {'error': 'Password must be at least 8 characters'})
        if user_data.objects.filter(email=a2).exists():         # ← prevents duplicate emails
            return render(request, 'signup.html', {'error': 'Email already registered'})
        data=user_data(name=a1,email=a2,contact=a3,password=a4)
        data.save()
        return redirect('login')
    return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        b1=request.POST['email']
        b2=request.POST['password']
        obj=user_data.objects.filter(email=b1,password=b2)
        if obj:
            request.session['user']=b1
            return redirect("/index/")
        else:
            return HttpResponse("Invalid Response")
    return render(request,'login.html')
def logout(request):
    request.session.flush()   # ← clears session
    return redirect('login')