from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Teacher
from .forms import TeachersAddForm


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


def teachers_add(request):
    if request.method == "POST":
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeachersAddForm()
    return render(request, 'persons_add.html', context={"form": form})
