from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):
    help = 'Generates 100 random student'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--count',
                            help='Count students')

    def handle(self, *args, **options):
        count = int(options.get('count') or 100)
        i = 1
        while i <= count:
            Student.create_student()
            i += 1
        last_created_student = Student.objects.last()
        first_created_student = Student.objects.get(pk=last_created_student.pk-count-1)
        self.stdout.write(
            self.style.SUCCESS(
                f'''Successfully create {count} random student
                First student data:
                full name - \t{first_created_student.last_name} {first_created_student.first_name}
                birth date - \t{first_created_student.birth_date}
                E-mail - \t{first_created_student.email}
                phone - \t{first_created_student.phone}
                address - \t{first_created_student.address}
                .
                .
                .
                Last student data:
                full name - \t{last_created_student.last_name} {last_created_student.first_name}
                birth date - \t{last_created_student.birth_date}
                E-mail - \t{last_created_student.email}
                phone - \t{last_created_student.phone}
                address - \t{last_created_student.address}'''
                )
            )
