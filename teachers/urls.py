from django.urls import path

from . import views
import students.views as students_views


urlpatterns = [  
    path('teacher/', views.get_teacher, name='get_teacher'),
    path('teachers/', students_views.get_tracker, name='get_teachers'),
]