from django.conf.urls import url
from designers import views


urlpatterns=[
    url('manage_designers/',views.managedesigners),
    url('view_designers/',views.viewdesigners),
    # url('register_designer/',views.desiner_register),
    url('register_designer',views.desiner_register),
    url('Accept/(?P<idd>\w+)',views.Accept),
    url('Reject/(?P<idd>\w+)',views.Reject),
    url('view_designer_customer/',views.viewdesigners_customer),
]