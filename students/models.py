from datetime import date, datetime
from random import randrange

from django.db import models
from django.db.models import Q

from .fields import JSONField
from faker import Faker

from teachers.models import Teacher


class Student(models.Model):
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
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @classmethod
    def generate_person(cls):
        fake = Faker()
        cls.student = cls(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    birth_date=fake.simple_profile(sex=None).get('birthdate'),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    address=fake.simple_profile(sex=None).get('address')
                )
        cls.student.save()

    @classmethod
    def persons_filter(cls, queryset, query_str):
        if query_str:
            return queryset.filter(
                Q(first_name__contains=query_str)
                | Q(last_name__contains=query_str)
                | Q(email__contains=query_str)
            )


class Group(models.Model):
    DEPARTMENT = (
        ('E', 'Electrification'),
        ('M', 'Mechanics'),
        ('BT', 'Bridges and tunnels'),
        ('IT', 'Information Technology'),
    )
    YEAR_CHOICES = [(r, r) for r in range(1980, date.today().year+1)]

    number = models.PositiveSmallIntegerField()
    created_year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=datetime.now().year)
    department = models.CharField(
        max_length=3,
        choices=DEPARTMENT,
        default='E')
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
    message_file = models.FileField(
        blank=True, null=True,
        upload_to='messages/')

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f'{self.email}'
