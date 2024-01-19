from django.http import HttpResponseRedirect
from django.shortcuts import render
from payment.models import Payment
from orders.models import Orders
# Create your views here.
def postpayments(request,idd):
    obk=""
    obb=Orders.objects.get(orders_id=idd)

    ss = request.session['u_id']
    if request.method == 'POST':
        obj = Payment()
        obj.customer_id =ss
        obj.order_id=idd
        obj.amount=request.POST.get('Amount')
        obj.save()
        obk="kk"
    context = {
            'x': obb,
            'msg':obk
        }
        # return HttpResponseRedirect('/temp/home/')
    return render(request,'payment/post_payments.html',context)
def viewpayments(request):
    obj =Payment.objects.all()
    context = {
        'x': obj
    }
    return render(request,'payment/View_payments.html',context)

def viewpaymentcust(request):
    ss = request.session['u_id']
    obj = Payment.objects.filter(customer_id=ss)
    # obj = Payment.objects.all()
    context = {
        'x': obj
    }
    return render(request,'payment/view_payments_customer.html',context)
