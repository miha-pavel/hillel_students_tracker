from django.shortcuts import render
from django.db.models import Q


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
    query_str = request.GET.get('query_str')
    if query_str:
        # __contains LIKE %{}%
        queryset = queryset.filter(
            Q(first_name__contains=query_str)
            | Q(last_name__contains=query_str)
            | Q(email__contains=query_str)
        )
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
    # print('queryset: ', queryset.query)
    
    return render(
        request,
        'persons_list.html',
        context={'persons_type': 'students', 'persons_list': response}
        )
