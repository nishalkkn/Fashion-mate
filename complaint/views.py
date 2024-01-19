from django.http import HttpResponseRedirect
from django.shortcuts import render
from complaint.models import Complaint
# Create your views here.


def postcomplaint(request):
    ss = request.session['u_id']
    if request.method == 'POST':
        obj = Complaint()
        obj.customer_id = ss
        obj.complaint = request.POST.get('COMPLAINTS')
        obj.save()
        return HttpResponseRedirect('/temp/home/')
    return render(request,'complaint/post_complaints.html')

def postreplay(request,idd):
    if request.method == 'POST':
        obj = Complaint.objects.get(complaint_id=idd)
        obj.replay = request.POST.get('REPLAY')
        obj.save()
        # return HttpResponseRedirect('/temp/designers/')
        return viewcomplaintsdesigner(request)
    return  render(request,'complaint/post_replay.html')


def viewcomplaintsadmin(request):
    obj = Complaint.objects.all()
    context = {
        'x': obj
    }

    return  render(request,'complaint/view_complaints_admin.html',context)


def viewcomplaintscustomer(request):
    ss = request.session['u_id']
    obj =Complaint.objects.filter(customer_id=ss)
    context = {
        'x': obj
    }
    return render(request,'complaint/view_complaints_customer.html',context)
def viewcomplaintsdesigner(request):
    obj = Complaint.objects.all()
    context = {
        'x': obj
    }
    return render(request,'complaint/View_complaints_designer.html',context)
