from django.conf.urls import url
from assign import views
urlpatterns=[
    url('post_assign/', views.assigndeliveryboy),
    url('view_custmore/',views.viewassigncustomer),
    url('view_designer/',views.viewassigndesigner),
    url('Delivered/(?P<idd>\w+)',views.delivery),
    # url('Not Delivered/(?P<idd>\w+)',views.not_delivery),
    url('not_delivered/(?P<idd>\w+)',views.not_delivered),

    url('viw_asgn_delboy/',views.viw_assign_delboy),


]