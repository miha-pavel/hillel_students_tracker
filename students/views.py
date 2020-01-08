from django.shortcuts import render
from django.db.models import Q

from .models import Student, Group
from teachers.models import Teacher


def home_page(request):
    return render(request, 'base.html')


def get_student(request):
    Student.create_person()
    return render(
        request,
        'person_data.html',
        context={'person_type': 'student', 'person': Student.objects.last()}
        )


def get_group(request):
    Group.create_group()
    return render(
        request,
        'group_data.html',
        context={'group': Group.objects.last()}
        )


def persons_filter(queryset, query_str):
    print('query_str: ', query_str)
    if query_str:
        return queryset.filter(
            Q(first_name__contains=query_str)
            | Q(last_name__contains=query_str)
            | Q(email__contains=query_str)
        )


def get_tracker(request):
    full_url = request.build_absolute_uri('?')
    absolute_root = request.build_absolute_uri('/')[:-1].strip("/")
    request_type = full_url.split(absolute_root)[1].split("/")[1]
    queryset = []
    response = ''
    query_str = request.GET.get('query_str')
        # __endswith LIKE %{}
        # queryset = queryset.filter(first_name__endswith=fn)
        # __startswith LIKE {}%
        # queryset = queryset.filter(first_name__startswith=fn)
        #Регистронезависимое
        # __contains ILIKE %{}%
        # queryset = queryset.filter(first_name__icontains=fn)
        # __endswith ILIKE %{}
        # queryset = queryset.filter(first_name__iendswith=fn)
        # __startswith ILIKE {}%
        # queryset = queryset.filter(first_name__istartswith=fn)
    if request_type == 'students':
        queryset = Student.objects.all()
        if query_str:
            queryset = persons_filter(Student.objects.all(), query_str)
    elif request_type == 'teachers':
        queryset = Teacher.objects.all()
        if query_str:
            queryset = persons_filter(Teacher.objects.all(), query_str)
    elif request_type == 'groups':
        queryset = Group.objects.all()
        if query_str:
            queryset = queryset.filter(number__startswith=query_str)
    for queryset_item in queryset:
        response += queryset_item.get_info()+'<br>'
    # print('queryset: ', queryset.query)
    
    return render(
        request,
        'tracker_list.html',
        context={'tracker_type': request_type, 'tracker_list': response}
        )
