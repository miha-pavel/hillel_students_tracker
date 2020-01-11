from django.forms import ModelForm
from .models import Student


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        