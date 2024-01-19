from django.conf.urls import url
from deliveryboy import views



urlpatterns=[
    url('post_delivery_boy_register/',views.deliveryboy),
    url('view_delivery_boy/',views.viewdeliveryboy),
    url('viewdeliveryboy_designer/',views.viewdeliveryboy_designer),

]