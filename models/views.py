from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models.models import Models
from materials.models import Materials
# Create your views here.
def postmodels(request):
    obb=Materials.objects.all()
    context={
        'x':obb
    }
    if request.method == 'POST':
        obj = Models()
        obj.model= request.POST.get('models')
        # obj.uplode_image=request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.uplode_image = myfile.name
        obj.material_id=request.POST.get('vv')
        obj.amount=request.POST.get('am')
        obj.gender=request.POST.get('gen')
        obj.colour=request.POST.get('clr')
        obj.save()
        return HttpResponseRedirect('/temp/designers/')
    return render(request,'models/post_models.html',context)


def viewmodels(request):
    if request.method=='POST':
        vv=request.POST.get('lop')
        obj = Models.objects.filter(model__icontains=vv)
        context = {
            'x': obj
        }
        return render(request, 'models/VIEW_models.html',context)
    else:
        obj = Models.objects.filter(gender='female')
        context = {
            'x': obj
        }
    return render(request,'models/VIEW_models.html',context)

def v_men(request):
    obj = Models.objects.all()
    context = {
        'x': obj
    }


    return render(request, 'models/view_men.html', context)