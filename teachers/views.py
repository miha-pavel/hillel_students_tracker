from django.shortcuts import render
from django.db.models import Q

from .models import Teacher


def get_teacher(request):
    Teacher.create_person()
    return render(
        request,
        'person_data.html',
        context={'person_type': 'teacher', 'person': Teacher.objects.last()}
        )


def get_teachers(request):
    queryset = Teacher.objects.all()
    response = ''
    query_str = request.GET.get('query_str')
    if query_str:
        queryset = queryset.filter(
            Q(first_name__contains=query_str)
            | Q(last_name__contains=query_str)
            | Q(email__contains=query_str)
        )
    for teacher in queryset:
        response += teacher.get_info()+'<br>'
    return render(
        request,
        'persons_list.html',
        context={'person_type': 'teachers', 'persons_list': response}
        )
