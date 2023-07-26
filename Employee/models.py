from django.db import models

# Create your models here.
class Employee(models.Model):
    FirstName=models.CharField(max_length=100)
    MiddleName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    DOB=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=200)
    Pincode=models.IntegerField()
    Nationality=models.CharField(max_length=100)
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    ConfirmPass=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)


    def __str__(self):
        return self.FirstName+''+self.LastName


class EmpPayment(models.Model):
    MonthSalary=models.CharField(max_length=100)
    WorkingDays=models.CharField(max_length=100)
    BasicSalary=models.CharField(max_length=100)
    HRASalary=models.CharField(max_length=100)
    MediClaimSalary=models.CharField(max_length=100)
    TASalary=models.CharField(max_length=200)
    DASalary=models.CharField(max_length=200)
    ReimbursementSalary=models.CharField(max_length=200)
    CASalary=models.CharField(max_length=100)
    DPFSalary=models.CharField(max_length=100)
    DTAXSalary=models.CharField(max_length=100)
    DeductionSalary=models.CharField(max_length=100)
    Total=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)

    def __str__(self):
        return self.Name
