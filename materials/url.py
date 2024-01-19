from django.conf.urls import url
from materials import views



urlpatterns=[
    url('postmaterials/',views.postmaterials),
    url('viewmaterials/',views.viewmaterials),
]
