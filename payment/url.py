from django.conf.urls import url
from payment import views
urlpatterns=[
    url('postpayment/(?P<idd>\w+)',views.postpayments),
    url('viewpayment/',views.viewpayments),
    url('viewpaymentscust/',views.viewpaymentcust),
]