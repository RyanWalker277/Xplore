import email
import http
from django.shortcuts import render 
from .models import Data
from .models import StudentData
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request , 'index.html')

def login(request):
    return render(request , 'login.html')

def purchase(request):
    return render(request , 'purchase.html')

def register(request):
    return render(request , 'register.html')

def dashboard(request):
    return render(request , 'dashboard.html')

def search_result(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            data = Data.objects.filter(college_name__icontains=query) 
            return render(request, 'search_result.html', {'data':data})
        else:
            print("No information to show")
            return render(request, 'search_result.html', {})

def kiet_page(request):
    return render(request , 'kiet.html')

def done(request):
    return render(request , 'done.html')

def profile_settings(request):
    return render(request , 'profile_settings.html')

def save(request):

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        marks10 = request.POST.get('marks10')
        marks12 = request.POST.get('marks12')

        en = StudentData(First_Name = firstname ,Last_Name = lastname , Email = email , Class_10_marks = marks10 , Class_12_marks = marks12 )
        en.save()

    return render(request , 'details_saved.html')