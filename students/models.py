import datetime

from django.db import models

from faker import Faker


fake = Faker()


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    phone = models.CharField(max_length=16) #clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    @classmethod
    def generate_student(cls):
        return cls(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    birth_date=fake.simple_profile(sex=None).get('birthdate'),
                    email=fake.simple_profile(sex=None).get('mail'),
                    phone=fake.phone_number(),
                    address=fake.simple_profile(sex=None).get('address')
                )

    @classmethod
    def create_student(cls):
        cls.generate_student().save()


class Group(models.Model):
    DEPARTMENT = (
        ('E', 'Electrification'),
        ('M', 'Mechanics'),
        ('BT', 'Bridges and tunnels'),
        ('IT', 'Information Technology'),
    )
    YEAR_CHOICES = [(r, r) for r in range(1980, datetime.date.today().year+1)]

    number = models.CharField(max_length=10, unique=True)
    created_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    department = models.CharField(max_length=3, choices=DEPARTMENT, default='E')
    specialty_number = models.PositiveSmallIntegerField()
    specialty_name = models.CharField(max_length=255)
    #Statistic
    skipped_classes = models.PositiveSmallIntegerField()
    min_rating = models.PositiveSmallIntegerField()
    max_rating = models.PositiveSmallIntegerField()
    average_rating = models.DecimalField(max_digits=5, decimal_places=2)
    standard_deviation_rating = models.DecimalField(max_digits=5, decimal_places=2)
    mode_rating = models.DecimalField(max_digits=5, decimal_places=2)
    median_rating = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return f'{self.number}'
