from django.shortcuts import render

from .models import Student


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
    
    return render(
        request,
        'persons_list.html',
        context={'person_type': 'students', 'persons_list': response}
        )
