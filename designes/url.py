from django.conf.urls import url
from designes import views



urlpatterns=[
    url('post_designes/',views.post_designs),
    url('viwe_designes/',views.view_designes),
]