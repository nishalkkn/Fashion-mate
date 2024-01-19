from django.http import HttpResponseRedirect
from django.shortcuts import render
from designers.models import Designers
from  login.models import Login

# Create your views here.
def managedesigners(request):
    obj = Designers.objects.all()
    context={
        'x':obj
    }
    return render(request,'designers/manage_designer.html',context)


def viewdesigners(request):
    obj = Designers.objects.all()
    context = {
        'x': obj
    }
    return render(request,'designers/view_designer_customer.html',context)


def desiner_register(request):
    ss = request.session['u_id']
    if request.method == 'POST':
        obj = Designers()
        var = Login()

        obj.designers_name = request.POST.get('name')
        obj.email=request.POST.get('Email')
        obj.phone_no = request.POST.get('Phone no')
        obj.password = request.POST.get('Password')
        obj.status='pending'
        obj.save()

        var.email = obj.email
        var.password = obj.password
        var.u_id = obj.designers_id
        var.type = "designer"
        var.save()

        return HttpResponseRedirect('/login/postloign/')

    return render(request,'designers/post_register_designer.html')

def Accept(request,idd):
    obb=Designers.objects.get(designers_id=idd)
    obb.status="Accept"
    obb.save()
    return managedesigners(request)

def Reject(request,idd):
    obb=Designers.objects.get(designers_id=idd)
    obb.status="Reject"
    obb.save()
    return managedesigners(request)

def viewdesigners_customer(request):
    ss = request.session['u_id']
    obj = Designers.objects.filter(desiner_id=ss)
    obj = Designers.objects.all()
    context = {
        'x': obj
    }
    return render(request,'designers/view_designer_customer.html',context)



