from django.urls import path

from . import views


urlpatterns = [
    path('gen/', views.get_teacher, name='get_teacher'),
    path('list/', views.get_teachers, name='get_teachers'),
    path('add/', views.teacher_add, name='teacher_add'),
    path('edit/<int:pk>/', views.teacher_edit, name='teacher_edit'),
    path('delete/<int:pk>/', views.teacher_delete, name="teacher_delete"),
]
