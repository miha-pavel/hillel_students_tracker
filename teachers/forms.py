from django.forms import ValidationError

from .models import Teacher
from students.forms import BaseStudentForm


class TeachersAddForm(BaseStudentForm):

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'email')

    def clean_email(self):
        email = self.cleaned_data['email'].lower() # то что пришло с формы
        # filter(email=email) -> filter(email__exact=email)
        # email должен быть регистронезависимым ->email__iexact
        email_exists = Teacher.objects\
            .filter(email__iexact=email)\
            .exclude(email__iexact=self.instance.email)
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email
