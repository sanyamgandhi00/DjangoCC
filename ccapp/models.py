# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator

year_choices = ( 
    ("FY","FY"), 
    ("SY","SY"), 
    ("TY","TY"), 
    ("LY","LY"), 
) 

branch_choices = ( 
    ("IT","IT"), 
    ("COMPS","COMPS"), 
    ("EXTC","EXTC"), 
    ("ETRX","ETRX"), 
    ("MECH","MECH"), 
) 

#signup details
class Seller(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    fullName = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)
    contactNumber= models.CharField(max_length=12)
    year=models.CharField(max_length = 2, choices = year_choices, default = 'FY') 
    branch=models.CharField(max_length = 5, choices =branch_choices, default = 'IT') 
    #Image = models.ImageField(upload_to="images/customer/profile/", null=True, blank=True,default="images/customer/profile/default-customer.png")


class Customer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    fullName = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)
    contactNumber= models.CharField(max_length=12)
    year=models.CharField(max_length = 2, choices = year_choices, default = 'FY') 
    branch=models.CharField(max_length = 5, choices =branch_choices, default = 'IT') 


#products

book_status=( 
    ("pending","pending"),
    ("verified","verified"),
    ("inProcess","inProcess"),
    ("sold","sold"),
) 
class Book(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE,related_name="books")
    bookName=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField(blank=True)
    status=models.CharField(max_length = 10, choices = book_status, default = 'pending') 
    timestamp=models.DateTimeField(auto_now_add=True)

coat_status=(
    ("inStock","inStock"),
    ("inProcess","inProcess"),
    ("sold","sold"),
)
size_choices=(
    ("S","S"),
    ("M","M"),
    ("L","L"),
    ("XL","XL"),
    ("XXL","XXL"),
    ("XXXL","XXXL"),
)
class Coat(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE,related_name="coats")
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField(blank=True)
    size=models.CharField(max_length = 10, choices = size_choices, default = 'L') 
    gender=models.CharField(max_length = 10, choices =(("M","M"),("F","F")), default = 'M') 
    status=models.CharField(max_length = 10, choices = coat_status, default = 'inStock')
    old=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)


class Calculator(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE,related_name="calculators")
    modelNumber=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    old=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)



#Order

class Order_Book(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="order_books")
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="order_books")
    timestamp=models.DateTimeField(auto_now_add=True)

class Order_Coat(models.Model):
    coat=models.ForeignKey(Coat,on_delete=models.CASCADE,related_name="order_coats")
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="order_coats")
    timestamp=models.DateTimeField(auto_now_add=True)

class Order_Calculator(models.Model):
    calculator=models.ForeignKey(Calculator,on_delete=models.CASCADE,related_name="order_calculators")
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="order_calculators")
    timestamp=models.DateTimeField(auto_now_add=True)

#feedbacks

class Report_Book(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="report_books")
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="report_books")

class Feedback(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    feedback=models.TextField()
    year=models.CharField(max_length = 2, choices = year_choices, default = 'FY') 
    branch=models.CharField(max_length = 5, choices =branch_choices, default = 'IT')
