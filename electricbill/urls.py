"""electricbill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from frontendpage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userlogin, name='userlogin'),
    path('userhomepage', userhomepage , name='userhomepage'),
    path('adminlogin', adminlogin, name='adminlogin'),
    path('adminhome', adminhome, name='adminhome' ),
    path('addbill', addbill, name='addbill' ),
    path('addBillUser', addBillUser, name='addBillUser'),
    path('addconnection', addconnection, name='addconnection'),
    path('addcustomer',addcustomer, name='addcustomer'),
    path('viewbill',viewbill,name='viewbill'),
    path('viewconnection',viewconnection,name='viewconnection'),
    path('viewcustomer',viewcustomer, name='viewcustomer'),
    path('logout', Logout, name='logout'),
    path('viewmybill',viewmybill, name='viewmybill'),
    path('deletebill/<int:pid>', deletebill, name='deletebill'),
    path('payment/<int:pid>', payment, name='payment'),

]
