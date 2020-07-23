from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User,auth
from .models import Seller , Customer
from .forms import SellerForm , CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import re

# Create your views here.
def index(request):
    return render(request,"index.html")


def sellerSignUp(request):          
    context = {}
    if request.method == 'POST':
        s_form = SellerForm(request.POST)
        context['s_form'] = s_form
        print(context)
        if s_form.is_valid():
            print("Valid")

            username = s_form.cleaned_data.get('username')
            print(username)
            password = s_form.cleaned_data.get('Password')
            Email = s_form.cleaned_data.get('email')
            if User.objects.filter(email=Email).exists():
                print("Exist")
                messages.info(request, 'Email already exists')
                return HttpResponse('customer1')
            elif User.objects.filter(username=username).exists():
                print("Exist")
                messages.info(request, 'Username already exists')
                return HttpResponse('customer1')
            else:
                s_form.save()
                print("Saved")
                user = User.objects.create_user(username=username,password=password,email=Email)
                user.save()
                print('USerSaved')
            
                print("Done")
                
                return HttpResponse('customer1')
        else:
            return render(request, 'sellerSignUp.html', context)
    else:
        print("GET REQ")
        s_form = SellerForm()
        context['s_form'] = s_form
        return render(request, 'sellerSignUp.html', context)



def customerSignUp(request):          
    context = {}
    if request.method == 'POST':
        c_form = CustomerForm(request.POST)
        context['c_form'] = c_form
        print(context)
        if c_form.is_valid():
            print("Valid")

            username = c_form.cleaned_data.get('username')
            print(username)
            password = c_form.cleaned_data.get('Password')
            Email = c_form.cleaned_data.get('email')
            if User.objects.filter(email=Email).exists():
                print("Exist")
                messages.info(request, 'Email already exists')
                return HttpResponse('customer1')
            elif User.objects.filter(username=username).exists():
                print("Exist")
                messages.info(request, 'Username already exists')
                return HttpResponse('customer1')
            else:
                c_form.save()
                print("Saved")
                user = User.objects.create_user(username=username,password=password,email=Email)
                user.save()
                print('USerSaved')
            
                print("Done")
                
                return HttpResponse('customer1')
        else:
            return render(request, 'customerSignUp.html', context)
    else:
        print("GET REQ")
        c_form = CustomerForm()
        context['c_form'] = c_form
        return render(request, 'customerSignUp.html', context)




def login(request):
    if request.method=="POST":
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        
        if Customer.objects.filter(username=Username,password=Password).exists() :
            user = User.objects.get(username=Username)
            auth.login(request,user)
            if request.GET.get("next",None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponse('Logged In !!!!!! ')

        elif Seller.objects.filter(username=Username,password=Password).exists():
            user = User.objects.get(username=Username)
            auth.login(request, user)
            if request.GET.get("next",None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponse("Logged In !!")
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')
