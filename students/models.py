from datetime import date, datetime
from random import randrange

from django.db import models
from django.db.models import Q

from faker import Faker

from .fields import JSONField
from teachers.models import Teacher
from students import model_choices as mch


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    group = models.ForeignKey(
        'students.Group',
        null=True, blank=True,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    @classmethod
    def generate_person(cls):
        fake = Faker()
        cls.student = cls(
                    first_name=fake.first_name().title(),
                    last_name=fake.last_name().title(),
                    birth_date=fake.simple_profile(sex=None).get('birthdate'),
                    email=fake.email(),
                    phone=int(''.join([n for n in fake.phone_number() if n.isdigit()])),
                    address=fake.simple_profile(sex=None).get('address')
                )
        cls.student.save()
        return cls.student

    @classmethod
    def persons_filter(cls, queryset, query_str):
        if query_str:
            return queryset.filter(
                Q(first_name__contains=query_str)
                | Q(last_name__contains=query_str)
                | Q(email__contains=query_str)
            )


class Group(models.Model):
    ELECTRIFICATION, MECHANICS, BRIDGES_TUNNELS, INFORMATION_TECHNOLOGY = 0, 1, 2, 3
    DEPARTMENT = (
        (ELECTRIFICATION, 'Electrification'),
        (MECHANICS, 'Mechanics'),
        (BRIDGES_TUNNELS, 'Bridges and tunnels'),
        (INFORMATION_TECHNOLOGY, 'Information Technology'),)

    YEAR_CHOICES = [(r, r) for r in range(1980, date.today().year+1)]

    number = models.PositiveSmallIntegerField()
    created_year = models.PositiveSmallIntegerField(
        choices=YEAR_CHOICES,
        default=datetime.now().year)
    department = models.PositiveSmallIntegerField(
        choices=DEPARTMENT,
        default=ELECTRIFICATION)
    specialty_number = models.PositiveSmallIntegerField(default=141)
    specialty_name = models.CharField(max_length=255, default='electrition')
    head_student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='head_student')
    head_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='head_teacher')

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return f'{self.number}'

    @classmethod
    def create_group(cls):
        number = int(f'{randrange(1, 10)}{randrange(1, 6)}{randrange(1, 10)}')
        group, _ = Group.objects.get_or_create(number=number)
        return group


class Message(models.Model):
    email = models.EmailField()
    message = JSONField()
    message_file = models.FileField(
        blank=True, null=True,
        upload_to='messages/')

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f'{self.email}'


class Logger(models.Model):
    GET, POST, DELETE, PUT, PATCH, HEAD, CONNECT, OPTIONS, TRACE = 0, 1, 2, 3, 4, 5, 6, 7, 8
    METHOD = (
        (GET, 'GET'), (POST, 'POST'), (DELETE, 'DELETE'), (PUT, 'PUT'), (PATCH, 'PATCH'),
        (HEAD, 'HEAD'), (CONNECT, 'CONNECT'), (OPTIONS, 'OPTIONS'), (TRACE, 'TRACE'),
        )
    METHODS_REVERSED_MAP = {name: id for id, name in METHOD}

    path = models.CharField(max_length=255)
    method = models.PositiveSmallIntegerField(
        choices=mch.METHOD,
        default=GET)
    ime_delta = models.PositiveSmallIntegerField()
    user_id = models.PositiveSmallIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Logger"
        verbose_name_plural = "Loggers"

    def __str__(self):
        return f'{self.path}'
