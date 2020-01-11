from django.shortcuts import render

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
        queryset = Teacher.persons_filter(Teacher.objects.all(), query_str)
    for queryset_item in queryset:
        response += queryset_item.get_info()+'<br>'
    return render(
        request,
        'tracker_list.html',
        context={'tracker_type': 'teacher', 'tracker_list': response}
        )
