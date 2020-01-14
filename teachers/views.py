from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Teacher
from .forms import TeachersAddForm


def get_teacher(request):
    Teacher.create_person()
    return render(
        request,
        'teacher_data.html',
        context={'teacher': Teacher.objects.last()}
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
        'teachers_list.html',
        context={'teachers_list': response}
        )


def teacher_add(request):
    if request.method == "POST":
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_teachers'))
    else:
        form = TeachersAddForm()
    return render(request, 'teacher_add.html', context={"form": form})


def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == "POST":
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_teachers'))
    else:
        form = TeachersAddForm(instance=teacher)

    return render(request, 'teacher_edit.html', context={"form": form, "pk": pk})
