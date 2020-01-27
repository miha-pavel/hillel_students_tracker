import json
import datetime
import io

from django.core.files import File
from django.forms import ModelForm, Form, ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django import forms

from .models import Student, Group, Message


class BaseStudentForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower() # то что пришло с формы
        print(self.instance.email)# то что есть
        # filter(email=email) -> filter(email__exact=email)
        # email должен быть регистронезависимым ->email__iexact
        email_exists = Student.objects\
            .filter(email__iexact=email)\
            .exclude(email__iexact=self.instance.email)
        print('email_exists: ', email_exists)
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email


class StudentsAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'email', 'phone', 'group')


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            'number',
            'created_year',
            'department',
            'specialty_number',
            'specialty_name',
            'head_student',
            'head_teacher'
        ]


class ContactForm(Form):
    email = forms.EmailField()
    subject = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    def save(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list)
        fname = f'{datetime.datetime.now()}.txt'
        in_memory_file = io.StringIO(str(data))
        message_file = File(in_memory_file, name=fname)
        data = json.dumps(data)
        Message.objects.create(email=email_from, message=data, message_file=message_file)
