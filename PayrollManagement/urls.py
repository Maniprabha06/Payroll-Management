"""
URL configuration for PayrollManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('registration',registration,name='registration'),
    path('log',log,name='log'),
    path('loggedin',loggedin,name='loggedin'),
    path('signup',signup,name='signup'),
    path('AddPay',AddPay,name='AddPay'),
    path('header',header,name='header'),
    path('cntus',cntus,name='cntus'),
    path('abtus',abtus,name='abtus'),
    path('test',test,name='test'),
    path('join',join,name='join'),
    path('Pay',Pay,name='Pay'),
    path('signup', signup, name='signup'),
]
