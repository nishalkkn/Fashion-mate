from django.http import HttpResponseRedirect
from django.shortcuts import render
from customer.models import Customer
from login.models import Login
# Create your views here.

def postcustomerregister(request):
    if request.method == 'POST':
        obj = Customer()
        var = Login()

        obj.customer_name = request.POST.get('customer_name')
        obj.email=request.POST.get('Email')
        obj.phone_no = request.POST.get('Phone_no')
        obj.password = request.POST.get('Password')
        obj.save()

        var.email = obj.email
        var.password = obj.password
        var.u_id = obj.customer_id
        var.type = "customer"
        var.save()

        return HttpResponseRedirect('/login/postloign/')

    return render(request, 'customer/post_cust register.html')

def viewcustomer(request):
    obj = Customer.objects.all()
    context = {
        'x': obj
    }

    return render(request,'customer/view_customer.html',context)
