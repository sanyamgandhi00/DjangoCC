from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Student, Book,Suit, Coat, Calculator, Order_Book,Order_Suit, Order_Coat, Order_Calculator, Order_Toolkit, Report_Book, Feedback, DeletedEmails

# Create your views here.
def index(request):
    return render(request,"index.html")


def login(request):
    err=""
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            if DeletedEmails.objects.filter(email=username).exists():
                err = 'Your account has been deleted.'
                spam=DeletedEmails.objects.all()
                for e in spam:
                    print(e)
                    Student.objects.filter(email=e.email).delete()
                    User.objects.filter(email=e.email).delete()
            else:
                auth.login(request, user)
                return redirect('buyAProduct')
        else:
           err = 'Input correct email and password'
    template_name = 'login.html'
    context={'err':err}
    return render(request, template_name,context)

def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    err=""
    if request.method == 'POST':
        email = request.POST.get('email')
        if Student.objects.filter(email = email).exists():
            err = 'Email already taken. Try a different one.'

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
    template_name = 'login.html'
    context={'err':err}
    return render(request, template_name,context)

@login_required(login_url="login")
def profile(request):
    email = request.user.username
    if request.method=='POST':
        # obj1 = User.objects.get(
        #     email = email,
        # )
        # obj1.set_password(request.POST.get('password'))
        # obj1.save()
        # password = request.POST.get('password')
        # confirmpassword = request.POST.get('confirmPassword')
        contactNumber = request.POST.get('contactNumber')
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        Student.objects.filter(email=email).update(
            # password = password,
            # confirmPassword = confirmpassword,
            contactNumber = contactNumber,
            year = year,
            branch = branch
        )
        # user = authenticate(request, username = request.user.email, password = request.POST.get('password'))
        # auth.login(request, user)
    template_name = 'profile.html'
    # print(request.user.email)
    # print(Student.objects.get(email=request.user.email).email)
    context={'student':Student.objects.get(email=email)}
    return render(request, template_name, context)


def buyAProduct(request):
    #delete spam email
    spam=DeletedEmails.objects.all()
    for e in spam:
        print(e)
        Student.objects.filter(email=e.email).delete()
        User.objects.filter(email=e.email).delete()
    books=Book.objects.filter(status="verified")
    template_name="buyAProduct.html"
    context={"books":books}
    return render(request,template_name,context)

@login_required(login_url="login")
def sellAProduct(request):
    books=Book.objects.filter(seller__email__contains=request.user.username)
    for book in books:
        print(book.bookId)
    template_name="sellAProduct.html"
    context={}
    return render(request,template_name,context)

@login_required(login_url="login")
def buyBook(request,bookId):
    customer=Student.objects.get(email=request.user.username)
    book=Book.objects.get(bookId=bookId)
    order_book_obj=Order_Book.objects.create(
        book=book,
        customer=customer
    )
    order_book_obj.save()
    status="inProcess"
    Book.objects.filter(bookId=bookId).update(status=status)
    print("timestamp: ",Order_Book.objects.get(book=book).timestamp)
    return redirect("buyAProduct")

@login_required(login_url="login")
def sellBook(request):
    email=request.user.username
    student=Student.objects.get(email=email)
    if request.method == "POST" and request.FILES['bookImage']:
        seller=student
        bookImage=request.FILES["bookImage"]
        bookName=request.POST["bookName"]
        author=request.POST["author"]
        price=request.POST["price"]
        description=request.POST["description"]
        status="pending"
        book_obj=Book.objects.create(
            seller=seller,
            bookImage=bookImage,
            bookName=bookName,
            author=author,
            price=price,
            description=description,
            status=status
        )
        book_obj.save()
    return redirect("sellAProduct")

@login_required(login_url="login")
def buySuit(request):
    if request.method == 'POST':
        customer=Student.objects.get(email=request.user.username)
        suit_gender=request.POST["suit-gender"]
        suit_size=request.POST["suit-size"]
        suit_condition=request.POST["suit-condition"]
        if(Suit.objects.filter(size=suit_size,gender=suit_gender,condition=suit_condition,status="inStock").exists()):
            suit1=Suit.objects.filter(size=suit_size,gender=suit_gender,condition=suit_condition,status="inStock")[0]
            suit_seller=suit1.seller.email
            Suit.objects.filter(seller__email__contains = suit_seller,size=suit_size,gender=suit_gender,condition=suit_condition,status="inStock").update(status="inProcess")
            suit_obj=Order_Suit(customer=customer,suit=suit1)
            suit_obj.save()
            template_name="unavailableProduct.html"
        else:
            template_name="unavailableProduct.html"
        return render(request,template_name)

@login_required(login_url="login")
def buyCoat(request):
    if request.method == 'POST':
        customer=Student.objects.get(email=request.user.username)
        coat_size=request.POST["coat-size"]
        coat_condition=request.POST["coat-condition"]
        if(Coat.objects.filter(size=coat_size, condition=coat_condition, status="inStock").exists()):
            coat1=Coat.objects.filter(size=coat_size, condition=coat_condition,status="inStock")[0]
            coat_seller=coat1.seller.email
            Coat.objects.filter(seller__email__contains = coat_seller,size=coat_size, condition=coat_condition,status="inStock").update(status="inProcess")
            coat_obj=Order_Coat(customer=customer, coat=coat1)
            coat_obj.save()
            template_name="unavailableProduct.html"
        else:
            template_name="unavailableProduct.html"
        return render(request,template_name)

@login_required(login_url="login")
def buyCalculator(request):
    if request.method == 'POST':
        customer=Student.objects.get(email=request.user.username)
        calculator_condition=request.POST["calculator-condition"]
        if(Calculator.objects.filter(condition=calculator_condition,status="inStock").exists()):
            calc1=Calculator.objects.filter(condition=calculator_condition,status="inStock")[0]
            calculator_seller=calc1.seller.email
            Calculator.objects.filter(seller__email__contains = calculator_seller, condition=calculator_condition,status="inStock").update(status="inProcess")
            calc_obj=Order_Calculator(customer=customer,calculator=calc1)
            calc_obj.save()
            template_name="unavailableProduct.html"
        else:
            template_name="unavailableProduct.html"
        return render(request,template_name)

@login_required(login_url="login")
def buyTool(request):
    if request.method == 'POST':
        customer=Student.objects.get(email=request.user.username)
        tool_obj=Order_Toolkit(customer=customer)
        tool_obj.save()
        template_name="unavailableProduct.html"
        return render(request,template_name)


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

