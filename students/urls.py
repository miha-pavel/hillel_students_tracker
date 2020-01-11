from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('student/', views.get_student, name='get_student'),
    path('students/', views.get_students, name='get_students'),
    path('students/add', views.students_add, name='students_add'),
    path('group/', views.get_group, name='get_group'),
    path('groups/', views.get_groups, name='get_groups'),
]
