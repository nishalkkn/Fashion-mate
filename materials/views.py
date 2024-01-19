from django.http import HttpResponseRedirect
from django.shortcuts import render
from materials.models import Materials
from django.core.files.storage import FileSystemStorage
# Create your views here.
def postmaterials(request):
    if request.method == 'POST':
        obj =Materials()
        obj.materials = request.POST.get('materials')
        # obj.uplod_image=request.POST.get('img')
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.uplod_image=myfile.name
        obj.gender=request.POST.get('gen')
        obj.save()
        return HttpResponseRedirect('/temp/designers/')

    return render(request,'materials/post_materials.html')

def viewmaterials(request):
    obj = Materials.objects.filter(gender='male')
    context = {
        'x': obj
    }
    return render(request,'materials/view_materials.html',context)


def viewmaterials_women(request):
    obj = Materials.objects.filter(gender='female')
    context = {
        'x': obj
    }
    return render(request,'materials/view_materials.html',context)


