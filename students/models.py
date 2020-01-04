from django.db import models

from faker import Faker


fake = Faker()


class Student(models.Model):
    '''
    '''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    phone = models.CharField(max_length=16) #clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    @classmethod
    def generate_student(cls):
        student = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.simple_profile(sex=None).get('birthdate'),
            email=fake.simple_profile(sex=None).get('mail'),
            phone=fake.phone_number()
        )
        student.save()
