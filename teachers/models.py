from django.db import models
from django.db.models import Q

from faker import Faker

# from students.models import Group


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True, blank=True)
    group = models.ForeignKey(
        'students.Group',
        null=True, blank=True,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    @classmethod
    def generate_person(cls):
        fake = Faker()
        return cls(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    birth_date=fake.simple_profile(sex=None).get('birthdate'),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    address=fake.simple_profile(sex=None).get('address')
                )

    @classmethod
    def create_person(cls):
        cls.generate_person().save()

    @classmethod
    def persons_filter(cls, queryset, query_str):
        if query_str:
            return queryset.filter(
                Q(first_name__contains=query_str)
                | Q(last_name__contains=query_str)
                | Q(email__contains=query_str)
            )

