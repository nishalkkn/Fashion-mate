from django.http import HttpResponseRedirect
from django.shortcuts import render
from feedback.models import Feedback
# Create your views here.
def postfeedback(request):
    ss = request.session['u_id']
    if request.method == 'POST':
        obj = Feedback()
        obj.customer_id = ss
        obj.feedback=request.POST.get('FEEDBACK')
        obj.save()
        return HttpResponseRedirect('/temp/home/')
    return render(request,'feedback/post_feedback.html')


def viewfeedback(request):
    ss = request.session['u_id']
    obj = Feedback.objects.filter(customer_id=ss)

    context = {
        'x': obj
    }
    return render(request,'feedback/view_feedback.html',context)


def viewfeedback_designer(request):
    obj = Feedback.objects.all()
    context = {
        'x': obj
    }
    return render(request,'feedback/view_feedback_designer.html',context)

