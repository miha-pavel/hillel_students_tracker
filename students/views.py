from django.shortcuts import render

from .models import Student


def get_student(request):
    Student.create_student()
    return render(request, 'student_data.html', {'student': Student.objects.last()})


def get_students(request):
    print('request.GET: ', request.GET)
    queryset = Student.objects.all()
    response = ''
    fn = request.GET.get('first_name')
    if fn:
        # __contains LIKE %{}%
        queryset = queryset.filter(first_name__contains=fn)
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
    for student in queryset:
        response += student.get_info()+'<br>'
    print('queryset: ', queryset.query)
    
    return render(request,
                'students_list.html',
                context={'students_list': response})
