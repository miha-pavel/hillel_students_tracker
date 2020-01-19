from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from annoying.decorators import render_to

from .models import Teacher
from .forms import TeachersAddForm


@render_to('teacher_data.html')
def get_teacher(request):
    Teacher.create_person()
    return {'teacher': Teacher.objects.last()}


@render_to('teachers_list.html')
def get_teachers(request):
    teachers = Teacher.objects.all()
    query_str = request.GET.get('query_str')
    if query_str:
        teachers = Teacher.persons_filter(Teacher.objects.all(), query_str)
    return {'teachers': teachers}


@render_to('teacher_add.html')
def teacher_add(request):
    if request.method == "POST":
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_teachers'))
    else:
        form = TeachersAddForm()
    return {"form": form}


@render_to('teacher_edit.html')
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == "POST":
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_teachers'))
    else:
        form = TeachersAddForm(instance=teacher)
    return {"form": form, "pk": pk}


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    teacher.delete()
    return HttpResponseRedirect(reverse('get_teachers'))
