from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from annoying.decorators import render_to

from .models import Student, Group
from .forms import StudentsAddForm, GroupsAddForm, ContactForm, SignupForm
from .tokens import account_activation_token
from .tasks import send_signup_email


def home_page(request):
    return render(request, 'base.html')


@render_to('student_data.html')
def get_student(request):
    Student.generate_person()
    return {'student': Student.objects.last()}


@render_to('students_list.html')
def get_students(request):
    students = Student.objects.all().order_by('-id')
    query_str = request.GET.get('query_str')
    if query_str:
        students = Student.persons_filter(students, query_str)
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
    # print('queryset: ', queryset.query)
    return {'students': students}


@render_to('student_add.html')
def student_add(request):
    if request.method == "POST":
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_students'))
    else:
        form = StudentsAddForm()
    return {"form": form}


@render_to('signup.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.is_active = False
            student.save()
            current_site = get_current_site(request)
            subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'student': student,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(student.pk)),
                'token': account_activation_token.make_token(student),
            })
            recipient = form.cleaned_data.get('email')
            send_signup_email.delay(subject=subject, message=message, to=recipient)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return {'form': form}


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        student = Student.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Student.DoesNotExist):
        student = None
    if student is not None and account_activation_token.check_token(student, token):
        student.is_active = True
        student.save()
        login(request, student)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


@render_to('student_edit.html')
def student_edit(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == "POST":
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_students'))
    else:
        form = StudentsAddForm(instance=student)
    return {"form": form, "pk": pk}


def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return HttpResponseRedirect(reverse('get_students'))


@render_to('contact.html')
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_students'))
    else:
        form = ContactForm()
    return {"form": form}


@render_to('group_data.html')
def get_group(request):
    Group.create_group()
    return {'group': Group.objects.last()}


@render_to('groups_list.html')
def get_groups(request):
    groups = Group.objects.all()
    groups = groups.select_related('head_student').select_related('head_teacher').order_by('number')
    query_str = request.GET.get('query_str')
    if query_str:
        groups = groups.filter(number__startswith=query_str)
    return {'groups': groups}


@render_to('group_add.html')
def group_add(request):
    if request.method == "POST":
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_groups'))
    else:
        form = GroupsAddForm()
    return {"form": form}


@render_to('group_edit.html')
def group_edit(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == "POST":
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_groups'))
    else:
        form = GroupsAddForm(instance=group)
    return {"form": form, "pk": pk}


def group_delete(request, pk):
    group = get_object_or_404(Group, id=pk)
    group.delete()
    return HttpResponseRedirect(reverse('get_groups'))
