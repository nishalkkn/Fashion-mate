from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('post_complaint/',views.postcomplaint),
    url('post_replay/(?P<idd>\w+)',views.postreplay),
    url('view_complaints_admin/',views.viewcomplaintsadmin),
    url('view_complaint_cust/',views.viewcomplaintscustomer),
    url('view_complaint_designer/',views.viewcomplaintsdesigner),
]