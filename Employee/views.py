from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from .models import EmpPayment
from .forms import EmployeeForm
from .forms import EmpPaymentForm

from django.contrib import messages
import manage


# Create your views here.
def output(request):
    data = manage.get


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, "Registration Success")
            return render(request, 'log.html', {})
        else:
            return render(request, 'loggedin.html', {})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form,
    })


def registration(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'registration.html', {})

    else:
        return render(request, 'registration.html', {})


def log(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'loggedin.html', {})
        else:
            messages.success(request, "Try again...")
            return render(request, 'signup.html', {})
    else:
        return render(request, 'log.html', {})


def loggedin(request):
    return render(request, 'loggedin.html')


def test(request):
    all_employee = Employee.objects.all

    return render(request, 'test.html', {'all': all_employee})


def Pay(request):
    all_Pay = EmpPayment.objects.all
    # val1 = int(request.GET["MonthSalary"])
    # val2 = int(request.GET["WorkingDays"])
    #
    # res = val1 + val2
    return render(request, 'Pay.html', {'all': all_Pay})


def join(request):
    return render(request, 'join.html', {})


def AddPay(request):
    if request.method == "POST":
        form = EmpPaymentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'AddPay.html', {})

    else:
        return render(request, 'AddPay.html', {})


def header(request):
    return render(request, 'header.html')


def abtus(request):
    return render(request, 'abtus.html')


def cntus(request):
    return render(request, 'cntus.html')
