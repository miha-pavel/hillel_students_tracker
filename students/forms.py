import json
import datetime
import io

from django.core.files import File
from django.forms import ModelForm, Form, ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django import forms
from django.core.validators import RegexValidator

from .models import Student, Group, Message


class BaseStudentForm(ModelForm):
    # phone_validator = RegexValidator(
    #     r'^\?1?\d{9,15}$',
    #     "This value may contain only number!"
    #     "Phone number must be entered in the format: '999999999'!")
    # phone = forms.IntegerField(validators=[phone_validator])

    def clean_email(self):
        email = self.cleaned_data['email'].lower() # то что пришло с формы
        # filter(email=email) -> filter(email__exact=email)
        # email должен быть регистронезависимым ->email__iexact
        email_exists = Student.objects\
            .filter(email__iexact=email)\
            .exclude(id=self.instance.id)
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].title()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].title()
        return last_name

    def clean_phone(self):
        phone = int(''.join([n for n in self.cleaned_data['phone'] if n.isdigit()]))
        return phone


class StudentsAddForm(BaseStudentForm):
    class Meta:
        model = Student
        # fields = ('id', 'first_name', 'last_name', 'birth_date', 'email', 'group', 'phone')
        fields = "__all__"


class StudentAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        # fields = ('id', 'first_name', 'last_name', 'birth_date', 'email', 'group')
        fields = "__all__"

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
