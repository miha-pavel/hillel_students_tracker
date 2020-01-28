from django.db import models
from django.db.models import Q

from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @classmethod
    def generate_person(cls):
        fake = Faker()
        cls.teacher = cls(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    birth_date=fake.simple_profile(sex=None).get('birthdate'),
                    email=fake.email(),
                    phone=int(''.join([n for n in fake.phone_number() if n.isdigit()])),
                    address=fake.simple_profile(sex=None).get('address')
                )
        cls.teacher.save()
        return cls.teacher

    @classmethod
    def persons_filter(cls, queryset, query_str):
        if query_str:
            return queryset.filter(
                Q(first_name__contains=query_str)
                | Q(last_name__contains=query_str)
                | Q(email__contains=query_str)
            )
