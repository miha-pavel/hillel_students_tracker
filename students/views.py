from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Student, Group
from .forms import StudentsAddForm, GroupsAddForm


def home_page(request):
    return render(request, 'base.html')


def get_student(request):
    Student.create_person()
    return render(
        request,
        'person_data.html',
        context={'person_type': 'student', 'person': Student.objects.last()}
        )


def get_students(request):
    queryset = Student.objects.all()
    response = ''
    query_str = request.GET.get('query_str')
    if query_str:
        queryset = Student.persons_filter(Student.objects.all(), query_str)
        # __endswith LIKE %{}
        # queryset = queryset.filter(first_name__endswith=fn)
        # __startswith LIKE {}%
        # queryset = queryset.filter(first_name__startswith=fn)
        # Регистронезависимое
        # __contains ILIKE %{}%
        # queryset = queryset.filter(first_name__icontains=fn)
        # __endswith ILIKE %{}
        # queryset = queryset.filter(first_name__iendswith=fn)
        # __startswith ILIKE {}%
        # queryset = queryset.filter(first_name__istartswith=fn)
    for queryset_item in queryset:
        response += queryset_item.get_info()+'<br>'
    # print('queryset: ', queryset.query)
    return render(
        request,
        'tracker_list.html',
        context={'tracker_type': 'student', 'tracker_list': response}
        )


def students_add(request):
    if request.method == "POST":
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentsAddForm()
    return render(request, 'persons_add.html', context={"form": form})


def get_group(request):
    Group.create_group()
    return render(
        request,
        'group_data.html',
        context={'group': Group.objects.last()}
        )


def get_groups(request):
    queryset = Group.objects.all()
    response = ''
    query_str = request.GET.get('query_str')
    if query_str:
        queryset = queryset.filter(number__startswith=query_str)
    for queryset_item in queryset:
        response += queryset_item.get_info()+'<br>'
    return render(
        request,
        'tracker_list.html',
        context={'tracker_type': 'Groups', 'tracker_list': response}
        )


def groups_add(request):
    if request.method == "POST":
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = GroupsAddForm()
    return render(request, 'groups_add.html', context={"form": form})
