from django.shortcuts import render

from .models import Student


def get_student(request):
    Student.generate_student()
    return render(request, 'student_data.html', {'student': Student.objects.last()})
    