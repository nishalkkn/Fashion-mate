from django.conf.urls import url
from customer import views


urlpatterns =[
    url('postcustomerregister/',views.postcustomerregister),
    url('viewcustomer/',views.viewcustomer),



]