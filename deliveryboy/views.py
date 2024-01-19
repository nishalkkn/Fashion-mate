from django.http import HttpResponseRedirect
from django.shortcuts import render
from deliveryboy.models import Deliveryboy
from login.models import Login
# Create your views here.
def deliveryboy(request):
    if request.method == 'POST':
        obj = Deliveryboy()
        var = Login()

        obj.name = request.POST.get('Delivery_boy_name')
        obj.email=request.POST.get('Email')
        obj.phone_no = request.POST.get('Phone_no')
        obj.password = request.POST.get('Password')
        obj.save()

        var.email = obj.email
        var.password = obj.password
        var.u_id = obj.deliveryboy_id
        var.type = "delivery boy"
        var.save()

        return HttpResponseRedirect('/login/postloign/')
    return render(request,'deliveryboy/post_delivery boy register.html')

def viewdeliveryboy(request):
    obj = Deliveryboy.objects.all()
    context = {
        'x': obj
    }
    return render(request,'deliveryboy/view_deliveryboy.html',context)

def viewdeliveryboy_designer(request):
    obj = Deliveryboy.objects.all()
    context = {
        'x': obj
    }
    return render(request,'deliveryboy/view_deliveryboy_designer.html',context)