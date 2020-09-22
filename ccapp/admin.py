from django.contrib import admin
from .models import Customer, Book, Coat, Calculator, Order_Book, Order_Coat, Order_Calculator, Report_Book, Feedback
# Register your models here.

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Coat)
admin.site.register(Calculator)
admin.site.register(Order_Book)
admin.site.register(Order_Coat)
admin.site.register(Order_Calculator)
admin.site.register(Report_Book)
admin.site.register(Feedback)
