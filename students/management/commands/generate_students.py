from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = 'Generates 100 random student'
    
    def handle(self, *args, **options):
        Student.generate_students()
        last_created_student = Student.objects.last()
        first_created_student = Student.objects.get(pk=last_created_student.pk-99)
        self.stdout.write(
            self.style.SUCCESS(
                f'''Successfully create 100 random student
                First student data:
                full name - \t{first_created_student.first_name} {first_created_student.last_name}
                birth date - \t{first_created_student.birth_date}
                E-mail - \t{first_created_student.email}
                phone - \t{first_created_student.phone}
                address - \t{first_created_student.address}
                .
                .
                .
                Last student data:
                full name - \t{last_created_student.first_name} {last_created_student.last_name}
                birth date - \t{last_created_student.birth_date}
                E-mail - \t{last_created_student.email}
                phone - \t{last_created_student.phone}
                address - \t{last_created_student.address}'''
                )
            )
