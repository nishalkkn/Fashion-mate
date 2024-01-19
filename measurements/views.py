from django.http import HttpResponseRedirect
from django.shortcuts import render
from measurements.models import Measurements
# Create your views here.
def post_measurements(request):
    ss=request.session['u_id']
    if request.method == 'POST':
        obj = Measurements()
        obj.way = request.POST.get('wayyy')
        obj.neck= request.POST.get('neckk')
        obj.shoulder= request.POST.get('shou')
        obj.bust= request.POST.get('bstt')
        obj.shoulder_to_bust= request.POST.get('bstshhh')
        obj.under_bust= request.POST.get('undrsww')
        obj.full_sleeve_length= request.POST.get('fulsss')
        obj.half_sleeve_length= request.POST.get('halffsss')
        obj.bicep= request.POST.get('biigg')
        obj.shoulder_to_hip= request.POST.get('shhip')
        obj.waist= request.POST.get('waddf')
        obj.hip= request.POST.get('ggg')
        obj.waist_to_knee= request.POST.get('olll')
        obj.knee= request.POST.get('kk')
        obj.inseam= request.POST.get('ddddd')
        obj.thigh= request.POST.get('thii')
        obj.cuff= request.POST.get('cuggg')
        obj.way= request.POST.get('wayyy')
        obj.customer_id=ss
        obj.save()
        return HttpResponseRedirect('/models/viewmodels/')
    return render(request,'measurements/post_measurement.html')


# def viewmeasurements(request):
# #     return render(request,'measurements/view_measurements.html')

def view_measurments(request):
    obj = Measurements.objects.all()
    context = {
        'x': obj
    }
    return render(request,'measurements/view_measurements.html',context)

