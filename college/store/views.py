from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import bio


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pswd']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bio')
        else:
            messages.info(request, 'invalid password')
            return redirect('login')
    return render(request, 'relo.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['txt']
        Email = request.POST['email']
        password = request.POST['pswd']

        user = User.objects.create_user(username=name, email=Email, password=password)
        user.save()
        messages.info(request, 'registered successfully')
    return render(request, 'relo.html')


def detail(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        DOB = request.POST.get('dob', )
        Age = request.POST.get('Age', )
        Gender = request.POST.get('Gender', )
        Phone = request.POST.get('Phone', )
        Email = request.POST.get('Email', )
        Address = request.POST.get("Address", )
        Department = request.POST.get('department', )
        Material = request.POST.getlist('material', )
        bio1 = bio(name=name, DOB=DOB, Age=Age, Gender=Gender, Phone=Phone, Email=Email, Address=Address,
                   Department=Department, Material=Material)
        bio1.save()

        messages.info(request, 'successfully submitted')
    return render(request, 'bio.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
