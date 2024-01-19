from django.http import HttpResponseRedirect
from django.shortcuts import render
from assign.models import Assign
from deliveryboy.models import Deliveryboy
from orders.models import Orders
from customer.models import Customer
# Create your views here.
def assigndeliveryboy(request):
    # ss = request.session['u_id']
    obb= Deliveryboy.objects.all()
    var=Orders.objects.all()
    context = {
        'a': obb,
        'b':var,

    }


    if request.method == 'POST':

        obj = Assign()
        obj.customer_id =1
        obj.deliveryboy_id= request.POST.get('deliveryboy_id')
        obj.order_id=request.POST.get('order_id')
        obj.delivery_status = "not delivered"
        obj.save()


        return HttpResponseRedirect('/temp/designers/')
    return render(request, 'assign/assign_delivery_boy.html',context)

def viewassigncustomer(request):
    ss = request.session['u_id']
    obj = Assign.objects.filter(order__customer_id=ss)
    # obj=Assign.objects.all()
    context={
        'x':obj
    }
    return render(request, 'assign/view_assign_customer.html',context)
def viewassigndesigner(request):
    obj = Assign.objects.all()
    context = {
        'x': obj
    }
    return render(request,'assign/view_assign_designer.html',context)


def viw_assign_delboy(request):
    ss = request.session['u_id']
    obj = Assign.objects.filter(deliveryboy_id=ss)
    # obj = Assign.objects.all()
    context = {
        'x': obj
    }
    return render(request,'assign/viw_asgn_dlvryboy.html',context)

def delivery(request,idd):
    obb = Assign.objects.get(assign_id=idd)
    obb.delivery_status = "Delivered"
    obb.save()
    return viw_assign_delboy(request)


# def not_delivery(request,idd):
#     obb = Assign.objects.get(assign_id=idd)
#     obb.delivery_status = "Not delivered"
#     obb.save()
#     return viw_assign_delboy(request)


def not_delivered(request,idd):
    obb = Assign.objects.get(assign_id=idd)
    obb.delivery_status = "Not delivered"
    obb.save()
    return viw_assign_delboy(request)