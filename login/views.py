from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
# Create your views here.
def postlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pasw = request.POST.get('password')
        obj = Login.objects.filter(email = email , password= pasw)
        typ= ""
        for var in obj:
            typ = var.type
            uid = var.u_id
            if typ == "admin":
                request.session['u_id'] =uid
                return HttpResponseRedirect('/temp/admin/')
            elif typ == "customer":
                request.session['u_id'] = uid
                return  HttpResponseRedirect('/temp/home/')
            elif typ == "delivery boy":
                request.session['u_id'] = uid
                return HttpResponseRedirect('/temp/deliveryboy/')
            elif typ == "designer":
                request.session['u_id'] = uid
                return HttpResponseRedirect('/temp/designers/')
            else:
                objlist ="Incorrect email or password.. try again!!!..."
                context = {
                    'msg':objlist,
                }
                return render(request, 'login/post_login.html', context)

    return render(request,'login/post_login.html')
