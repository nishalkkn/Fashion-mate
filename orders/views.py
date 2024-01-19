from django.http import HttpResponseRedirect
from django.shortcuts import render
from orders.models import Orders
# Create your views here.
def postorders(request,idd):
    ss = request.session['u_id']
    if request.method == 'POST':
        obj = Orders()
        obj.customer_id = ss
        obj.model_id = idd
        obj.quantity = request.POST.get('QUANTITY')
        obj.status = request.POST.get('status')
        obj.working_status= "pending"
        obj.save()
        # return HttpResponseRedirect('/measurmrnts/post_measrmrnts/')
    return render(request,'orders/post_order.html')

def manageorders(request):
    obj = Orders.objects.all()
    context = {
        'x': obj
    }

    if request.method == 'POST':
        obj = Orders()
        # obj.customer_id = 1
        # obj.deliveryboy_id = request.POST.get('deliveryboy_id')
        # obj.order_id = request.POST.get('order_id')
        obj.working_status = request.POST.get('working_status')
        # obj.status =
        obj.save()
        return HttpResponseRedirect('/temp/designers/')

    return render(request, 'orders/manage_order_designer.html', context)

def vieworders(request):
    obj = Orders.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'orders/view_order_admin.html', context)

def vieworderscustomer(request):
    ss = request.session['u_id']
    obj = Orders.objects.filter(customer_id=ss)
    # obj = Orders.objects.all()
    context = {
        'x': obj
    }
    return render(request,'orders/view_order_customer.html',context)

def approve(request,idd):
    obb=Orders.objects.get(orders_id=idd)
    obb.status="Approved"
    obb.save()
    return manageorders(request)

def cancelled(request,idd):
    obb=Orders.objects.get(orders_id=idd)
    obb.status="Cancelled"
    obb.save()
    return manageorders(request)



def stiching(request,idd):
    obb=Orders.objects.get(orders_id=idd)
    obb.working_status = "stiching"
    obb.save()
    return manageorders(request)


def packed(request,idd):
    obb=Orders.objects.get(orders_id=idd)
    obb.working_status = "packed"
    obb.save()
    return manageorders(request)


def shiped(request,idd):
    obb=Orders.objects.get(orders_id=idd)
    obb.working_status = "shiped"
    obb.save()
    return manageorders(request)






