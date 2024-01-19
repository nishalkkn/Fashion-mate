from django.conf.urls import url
from feedback import views



urlpatterns=[
    url('postfeedback/',views.postfeedback),
    url('viewfeedback/',views.viewfeedback),
    url('view_feedback_designer/',views.viewfeedback_designer),
]