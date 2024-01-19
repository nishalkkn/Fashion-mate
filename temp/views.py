from django.shortcuts import render
from materials.models import Materials
from models.models import Models
# Create your views here.


def admin(request):
    return render(request,'temp/admin.html')

def deliveryboy(request):
    return render(request,'temp/delivery boy.html')

def designers(request):
    return render(request,'temp/designers.html')

# def home(request):
#     obb = Materials.objects.all()
#     context = {
#         'x' : obb
#     }
#     return render(request, 'temp/customer.html', context)


def home(request):

    return render(request, 'temp/customer.html')

def secondpage (request):
    return render(request,'temp/secondpage.html')

def home_home(request):
    return render(request, 'temp/home_home.html')
def main_admin(request):
    return render(request,'temp/main_admin.html')

def main_customer(request):
    return render(request,'temp/main_customer.html')

def main_deliveryboy(request):
    return render(request,'temp/main_deliver_boy.html')

def main_designer(request):
    return render(request,'temp/main_designer.html')


def viewmodels(request):
    oobj = Models.objects.filter(gender='female')
    obj1 = Models.objects.filter(gender='male')
    context = {
        'y': oobj,
        'x': obj1
    }
    return render(request,'temp/customer.html',context)

def v_men(request):
    oobj = Models.objects.filter(gender='female')
    obj1 = Models.objects.filter(gender='male')
    context = {
        'y': oobj,
        'x': obj1
    }
    return render(request, 'temp/customer.html', context)

def female(request):
    obj = Models.objects.filter(gender='female')
    obj1 = Models.objects.filter(gender='male')
    context = {
        'y': obj,
        'x':obj1,

    }
    # print("total item",len(obj1))
    return render(request, 'temp/customer.html', context)





