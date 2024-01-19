from django.conf.urls import url
from models import views
urlpatterns=[
    url('postmodels/',views.postmodels),
    url('viewmodels/',views.viewmodels),
    url('men_view/', views.v_men)
]