from django.urls import path
from . import views


urlpatterns = [  
    path('', views.get_student, name='get_student'),
]