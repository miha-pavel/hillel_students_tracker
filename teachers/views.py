from django.shortcuts import render

from .models import Teacher


def get_teacher(request):
    Teacher.create_person()
    return render(
        request,
        'person_data.html',
        context={'person_type': 'teacher', 'person': Teacher.objects.last()}
        )
