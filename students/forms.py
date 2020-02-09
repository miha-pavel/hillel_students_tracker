import json
import datetime
import io

from django.core.files import File
from django.forms import ModelForm, Form, ValidationError
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
from django import forms


from .models import Student, Group, Message


class BasePersonForm(ModelForm):
    phone_regex = RegexValidator(
        regex=r'^\d{9,15}$',
        message="Phone number must be entered in the format: '999999999'.")
    phone = forms.CharField(validators=[phone_regex], max_length=15)

    def clean_email(self):
        # то что пришло с формы
        email = self.cleaned_data['email'].lower()
        # filter(email=email) -> filter(email__exact=email)
        # email должен быть регистронезависимым ->email__iexact
        email_exists = Student.objects\
            .filter(email__iexact=email)\
            .exclude(id=self.instance.id)
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_exists = Student.objects\
            .filter(phone__iexact=phone)\
            .exclude(id=self.instance.id)
        if phone_exists.exists():
            raise ValidationError(f'{phone} is already used!')
        return phone


class StudentsAddForm(BasePersonForm):

    class Meta:
        model = Student
        fields = "__all__"


class StudentAdminForm(BasePersonForm):
    class Meta:
        model = Student
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


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_password(self.cleaned_data['password'])
        super().save(commit)


class UserLoginForm(Form):
    username = forms.CharField()
    password = forms.CharField()
