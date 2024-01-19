from django.conf.urls import url
from temp import views
urlpatterns = [
    url('admin/',views.admin),
    url('deliveryboy/',views.deliveryboy),
    url('designers/',views.designers),
    url('home/',views.home),
    url('secondpage/',views.secondpage),
    url('not_registered/',views.home_home),
    url('main_admin/',views.main_admin),
    url('main_customer/',views.main_customer),
    url('main_deliveryboy/',views.main_deliveryboy),
    url('main_designer/',views.main_designer),
    url('abcd/',views.viewmodels),
    url('uuu/',views.v_men),
    url('female/',views.female)

]