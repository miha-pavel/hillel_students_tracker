from django.shortcuts import render

from .models import Teacher


def get_teacher(request):
    Teacher.create_person()
    return render(request, 'teacher_data.html', {'teacher': Teacher.objects.last()})


def get_teachers(request):
    queryset = Teacher.objects.all()
    response = ''
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__contains=fn)
    for teacher in queryset:
        response += teacher.get_info()+'<br>'
    
    return render(request,
                'teachers_list.html',
                context={'teachers_list': response})
