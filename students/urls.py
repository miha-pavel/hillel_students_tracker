from django.urls import path
from . import views


urlpatterns = [
    path('gen/', views.get_student, name='get_student'),
    path('list/', views.get_students, name='get_students'),
    path('add/', views.student_add, name='student_add'),
    path('edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('delete/<int:pk>/', views.student_delete, name="student_delete"),
    path('contact/', views.contact, name='contact'),
    path('group/', views.get_group, name='get_group'),
    path('groups/', views.get_groups, name='get_groups'),
    path('group_add/', views.group_add, name='group_add'),
    path('group_edit/<int:pk>/', views.group_edit, name='group_edit'),
    path('group_delete/<int:pk>/', views.group_delete, name="group_delete"),
]
