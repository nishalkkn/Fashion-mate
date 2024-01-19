# from django.conf.urls import url
# from measurements import views
# urlpatterns=[
#     url('post_measurements/',views.postmeasurements),
#     url('view_measurements/',views.viewmeasurements),
# ]

from django.conf.urls import url
from measurements import views
urlpatterns=[
    url('post_measrmrnts/',views.post_measurements),
    url('view_measurements/',views.view_measurments),
]