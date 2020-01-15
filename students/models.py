from datetime import date, datetime
from random import randrange

from django.db import models
from django.db.models import Q

from .fields import JSONField
from faker import Faker


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # TODO: add avatar
    # TODO: clean phone
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

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


class Student(Person):
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Group(models.Model):
    DEPARTMENT = (
        ('E', 'Electrification'),
        ('M', 'Mechanics'),
        ('BT', 'Bridges and tunnels'),
        ('IT', 'Information Technology'),
    )
    YEAR_CHOICES = [(r, r) for r in range(1980, date.today().year+1)]

    number = models.PositiveSmallIntegerField()
    created_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    department = models.CharField(max_length=3, choices=DEPARTMENT, default='E')
    specialty_number = models.PositiveSmallIntegerField(default=141)
    specialty_name = models.CharField(max_length=255, default='electrition')
    # Statistic
    skipped_classes = models.PositiveSmallIntegerField(blank=True, null=True)
    min_rating = models.PositiveSmallIntegerField(blank=True, null=True)
    max_rating = models.PositiveSmallIntegerField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    standard_deviation_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    mode_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    median_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return f'{self.number}'

    def get_info(self):
        return f'{self.number}'

    @classmethod
    def generate_group(cls):
        return cls(
            number=int(f'{randrange(1, 10)}{randrange(1, 6)}{randrange(1, 10)}'),
            )

    @classmethod
    def create_group(cls):
        generated_group = cls.generate_group()
        if not Group.objects.filter(number=generated_group.number).exists():
            cls.generate_group().save()


class Message(models.Model):
    email = models.EmailField()
    message = JSONField()

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f'{self.email}'
