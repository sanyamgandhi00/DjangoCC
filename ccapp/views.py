from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Student, Book, Coat, Calculator, Order_Book, Order_Coat, Order_Calculator, Report_Book, Feedback

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Input correct email and password')
    template_name = 'login.html'
    return render(request, template_name)

def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Student.objects.filter(email = email).exists():
            messages.error(request, 'Email already taken. Try a different one.')
        else:
            obj1 = User.objects.create(
                username = email,
                email = email,
            )
            obj1.set_password(request.POST.get('password'))
            obj1.save()
            fullName = request.POST.get('fullName')  
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmPassword')
            contactNumber = request.POST.get('contactNumber')
            year = request.POST.get('year')
            branch = request.POST.get('branch')
            obj2 = Student.objects.create(
                email = email,
                fullName = fullName,
                password = password,
                confirmPassword = confirmpassword,
                contactNumber = contactNumber,
                year = year,
                branch = branch
            )
            obj2.save()
            return redirect("login")
    return redirect("login")



'''def sellerSignUp(request):          
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
'''

