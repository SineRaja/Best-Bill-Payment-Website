from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from datetime import date
from django.contrib import messages

# Create your views here.

def userlogin(request):
    error = ""
    if request.method == 'POST':
        sd = request.POST['userdetails']
        pwd = request.POST['password']
        connection = Connection.objects.filter(customerconnectionid=sd).first()
        if connection is not None and connection.customeroccupation == pwd:  
            viewbill = Bill.objects.filter(connection=connection, status='Not Paid')
            return render(request, 'viewmybill.html', locals())
        else:
            messages.info(request, 'There is no user found!')
            return redirect('userlogin')
    return render(request,'userlogin.html', locals())

def userhomepage(request):
    return render(request, 'userhomepage.html')


def adminlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'adminlogin.html', locals())

def adminhome(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    cus = Customer.objects.all().count()
    conn = Connection.objects.all().count()
    b = Bill.objects.all().count()

    d = {'cus': cus, 'conn': conn, 'b': b}
    return render(request,'adminhome.html', d)


def addcustomer(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['userfirstname']
        ln = request.POST['userlastname']
        c = request.POST['usercontactnumber']
        e = request.POST['useremail']
        a = request.POST['useraddress']
        city = request.POST['usercity']
        s = request.POST['userstate']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=e)
            Customer.objects.create(user=user, usercontactnumber=c, useraddress=a, usercity=city, userstate=s)
            error = "no"
        except:
            error = "yes"
    return render(request,'addcustomer.html', locals())

def viewcustomer(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    customer = Customer.objects.all()
    return render(request,'viewcustomer.html', locals())

def addconnection(request):
    if not request.user.is_authenticated:
        return redirect(adminlogin)
    error = ""
    customer1 = Customer.objects.all()
    if request.method == "POST":
        cid = request.POST['connectionid']
        customerid = request.POST['customerid']
        ctype = request.POST['connectiontype']
        cdate = request.POST['connectionstartdate']
        o = request.POST['occupation']
        cload = request.POST['connectionload']
        pno = request.POST['plotno']
        c = request.POST['city']
        p = request.POST['pincode']
        a = request.POST['address']
        s = request.POST['state']
        d = request.POST['description']

        customer = Customer.objects.get(id=customerid)
        try:
            Connection.objects.create(customer=customer, customerconnectionid=cid, customerconnectiontype=ctype, customerconnectionstartdate=cdate, customeroccupation=o,
                                      customerconnectionload=cload, customerplotno=pno, customercity=c, customerpincode=p, customeraddress=a, customerstate=s, customerdescription=d)
            error = "no"
        except:
            error = "yes"
    return render(request,'addconnection.html', locals())

def viewconnection(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    connection = Connection.objects.all()
    return render(request,'viewconnection.html', locals())

def addbill(request):
    if not request.user.is_authenticated:
        return redirect(adminlogin)
    error = ""
    connection1 = Connection.objects.all()
    if request.method == "POST":
        usercnum = request.POST['connectionid']
        b = request.POST['newbilldate']
        cdreading = request.POST['currentdayreading']
        cpdreading = request.POST['previousdayreading']
        cnreading = request.POST['currentnightreading']
        cnpreading = request.POST['previousnightreading']
        cgreading = request.POST['currentgasreading']
        cgpreading = request.POST['previousgasreading']
        # t = request.POST['totalunit']
        cpud = request.POST['chargeperunitforday']
        cpun = request.POST['chargeperunitfornight']
        cpug = request.POST['chargeperunitforgas']
        cpuv = request.POST['stadingchargeper']
        fa = request.POST['finalamount']
        dd = request.POST['duedate']

        connection = Connection.objects.get(id=usercnum)
        try:
            Bill.objects.create(connection=connection, billformonth=b, 
                                dayelectricitycurrentreading=cdreading, dayelectricitypreviousreading=cpdreading,
                                dayelectricitychargeperunit=cpud, nightelectricitycurrentreading=cnreading, 
                                nightelectricitypreviousreading=cnpreading, nightelectricitychargeperunit=cpun,
                                gascurrentreading=cgreading, gaspreviousreading=cgpreading, 
                                gaschargeperunit=cpug, standingcharge=cpuv,  
                                finalamount=fa, duedate=dd, status='Not Paid')
            error = "no"
        except:
            error = "yes"
    return render(request,'addbill.html', locals())



def addBillUser(request):
    error = ""
    connection1 = Connection.objects.all()
    if request.method == "POST":
        usercnum = request.POST['connectionid']
        b = request.POST['newbilldate']
        cdreading = request.POST['currentdayreading']
        cpdreading = request.POST['previousdayreading']
        cnreading = request.POST['currentnightreading']
        cnpreading = request.POST['previousnightreading']
        cgreading = request.POST['currentgasreading']
        cgpreading = request.POST['previousgasreading']
        # t = request.POST['totalunit']
        cpud = request.POST['chargeperunitforday']
        cpun = request.POST['chargeperunitfornight']
        cpug = request.POST['chargeperunitforgas']
        cpuv = request.POST['stadingchargeper']
        fa = request.POST['finalamount']
        dd = request.POST['duedate']

        connection = Connection.objects.get(id=usercnum)
        try:
            Bill.objects.create(connection=connection, billformonth=b, 
                                dayelectricitycurrentreading=cdreading, dayelectricitypreviousreading=cpdreading,
                                dayelectricitychargeperunit=cpud, nightelectricitycurrentreading=cnreading, 
                                nightelectricitypreviousreading=cnpreading, nightelectricitychargeperunit=cpun,
                                gascurrentreading=cgreading, gaspreviousreading=cgpreading, 
                                gaschargeperunit=cpug, standingcharge=cpuv,  
                                finalamount=fa, duedate=dd, status='Not Paid')
            error = "no"
        except:
            error = "yes"
    return render(request,'addBillUser.html', locals())



def viewbill(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    bill = Bill.objects.all()
    return render(request,'viewbill.html', locals())

def deletebill(request,pid):
    bill = Bill.objects.get(id=pid)
    bill.delete()
    return redirect('viewbill')

def Logout(request):
    logout(request)
    return redirect('adminlogin')

def payment(request,pid):
    error = ""
    bill = Bill.objects.get(id=pid)
    x = bill.connection
    connection = Connection.objects.all()
    if request.method == "POST":
        bill.status = "paid"
        try:
            bill.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'pay.html', locals())

def viewmybill(request):
    return render(request,'viewmybill.html', locals())





