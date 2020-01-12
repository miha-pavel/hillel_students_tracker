from django.forms import ModelForm, Form
from django.core.mail import send_mail
from django.conf import settings
from django import forms

from .models import Student, Group


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            'number',
            'created_year',
            'department',
            'specialty_number',
            'specialty_name'
        ]


class ContactForm(Form):
    email = forms.EmailField(required=False)
    subject = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    def save(self):
        data = self.cleaned_datas

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list)
