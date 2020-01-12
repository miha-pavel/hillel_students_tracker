from django.forms import ModelForm
from .models import Teacher


class TeachersAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
