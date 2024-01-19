from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from designes.models import Designes
# Create your views here.
def post_designs(request):
    if request.method == 'POST':
        obj = Designes()
        obj.designers_id = request.POST.get('designers_id')
        obj.designes=request.POST.get('designes')
        # obj.images= request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.images = myfile.name
        obj.save()
        return HttpResponseRedirect('/temp/designers/')
    return render(request,'designes/post_designs.html')

def view_designes(request):
    obj = Designes.objects.all()
    context = {
        'x': obj
    }
    return render(request,'designes/view_designes.html',context)



