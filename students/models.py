from datetime import date
from django.db import models


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
    def generate_sudent(cls):
        student = cls(
            first_name='Pavlo2',
            last_name='Miha2',
            birth_date=date.now(),
            email='qwert@gmail.com',
            phone='1234576'
        )
        student.save()
