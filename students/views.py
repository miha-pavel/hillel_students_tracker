from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


from .models import Student, Group
from .forms import StudentsAddForm, GroupsAddForm, ContactForm


def home_page(request):
    return render(request, 'base.html')


def get_student(request):
    Student.create_person()
    return render(
        request,
        'student_data.html',
        context={'student': Student.objects.last()}
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
        'students_list.html',
        context={'student_list': response}
        )


def student_add(request):
    if request.method == "POST":
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_students'))
    else:
        form = StudentsAddForm()
    return render(request, 'student_add.html', context={"form": form})


def student_edit(request, pk):
    try:
        student = Student.objects.get(id=pk) #get_object_or_404
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with {pk} not found')

    if request.method == "POST":
        form = StudentsAddForm(request.POST, instance=student)# чтобы понимать кого редактировать
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_students'))
    else:
        form = StudentsAddForm(instance=student) #чтобы понимать кого взять для редактирования

    return render(request, 'student_edit.html', context={"form": form, "pk": pk})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_students'))
    else:
        form = ContactForm()
    return render(request, 'contact.html', context={"form": form})


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
        'groups_list.html',
        context={'groups_list': response}
        )


def group_add(request):
    if request.method == "POST":
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_groups'))
    else:
        form = GroupsAddForm()
    return render(request, 'group_add.html', context={"form": form})


def group_edit(request, pk):
    try:
        group = Group.objects.get(id=pk) # get_object_or_404
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group with {pk} not found')

    if request.method == "POST":
        form = GroupsAddForm(request.POST, instance=group) # чтобы понимать кого редактировать
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_Groups'))
    else:
        form = GroupsAddForm(instance=group) # понимать кого взять для редактирования

    return render(request, 'group_edit.html', context={"form": form, "pk": pk})
