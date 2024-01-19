from django.conf.urls import url
from orders import views
urlpatterns=[
    url('manageorders/',views.manageorders),
    url('postorders/(?P<idd>\w+)',views.postorders),
    url('vieworders/',views.vieworders),
    url('viewcustorders/',views.vieworderscustomer),
    url('approved/(?P<idd>\w+)',views.approve),
    url('cancelled/(?P<idd>\w+)',views.cancelled),
    url('stiching/(?P<idd>\w+)',views.stiching),
    url('packed/(?P<idd>\w+)', views.packed),
    url('shiped/(?P<idd>\w+)',views.shiped),

]