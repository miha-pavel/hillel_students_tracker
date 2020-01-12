from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('gen/', views.get_student, name='get_student'),
    path('list/', views.get_students, name='get_students'),
    path('add/', views.students_add, name='students_add'),
    path('edit/<int:pk>/', views.students_edit, name='students_edit'),
    path('contact/', views.contact, name='contact'),
    path('group/', views.get_group, name='get_group'),
    path('groups/', views.get_groups, name='get_groups'),
    path('groups_add/', views.groups_add, name='groups_add'),
    path('groups_edit/<int:pk>/', views.groups_edit, name='groups_edit'),
]
