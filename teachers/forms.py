from django.forms import ValidationError

from .models import Teacher
from students.forms import BasePersonForm


class TeachersAddForm(BasePersonForm):

    class Meta:
        model = Teacher
        fields = "__all__"

    def clean_email(self):
        # то что пришло с формы
        email = self.cleaned_data['email'].lower()
        # filter(email=email) -> filter(email__exact=email)
        # email должен быть регистронезависимым ->email__iexact
        email_exists = Teacher.objects\
            .filter(email__iexact=email)\
            .exclude(id=self.instance.id)
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email
