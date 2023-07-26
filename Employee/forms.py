from django import forms
from .models import Employee
from .models import EmpPayment


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['FirstName','MiddleName','LastName','DOB','Gender','Mobile','Address','Pincode','Nationality','UserName','Password','ConfirmPass','Email']

class EmpPaymentForm(forms.ModelForm):
    class Meta:
        model = EmpPayment
        fields = ['MonthSalary','WorkingDays','BasicSalary','HRASalary','MediClaimSalary','TASalary','DASalary','ReimbursementSalary','CASalary','DPFSalary','DTAXSalary','DeductionSalary','Total','Name']


