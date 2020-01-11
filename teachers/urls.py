from django.urls import path

from . import views


urlpatterns = [  
    path('teacher/', views.get_teacher, name='get_teacher'),
    path('teachers/', views.get_teachers, name='get_teachers'),
]
