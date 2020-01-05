from django.urls import path
from . import views


urlpatterns = [  
    path('student/', views.get_student, name='get_student'),
    path('students/', views.get_students, name='get_students'),
]
