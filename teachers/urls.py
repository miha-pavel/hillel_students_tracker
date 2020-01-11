from django.urls import path

from . import views


urlpatterns = [
    path('teacher/', views.get_teacher, name='get_teacher'),
    path('teachers/', views.get_teachers, name='get_teachers'),
    path('teachers/add', views.teachers_add, name='teachers_add'),
]
