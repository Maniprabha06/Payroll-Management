from django.contrib import admin


from .models import Employee
from .models import EmpPayment
admin.site.register(Employee)
admin.site.register(EmpPayment)