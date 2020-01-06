from django.core.management.base import BaseCommand

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates 100 random teacher'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--count',
                            help='Count teachers')

    def handle(self, *args, **options):
        count = int(options.get('count') or 100)
        i = 1
        while i <= count:
            Teacher.create_person()
            i += 1
        last_created_teacher = Teacher.objects.last()
        first_created_teacher = Teacher.objects.get(pk=last_created_teacher.pk-count-1)
        self.stdout.write(
            self.style.SUCCESS(
                f'''Successfully create {count} random teacher
                First teacher data:
                full name - \t{first_created_teacher.last_name} {first_created_teacher.first_name}
                birth date - \t{first_created_teacher.birth_date}
                E-mail - \t{first_created_teacher.email}
                phone - \t{first_created_teacher.phone}
                address - \t{first_created_teacher.address}
                .
                .
                .
                Last teacher data:
                full name - \t{last_created_teacher.last_name} {last_created_teacher.first_name}
                birth date - \t{last_created_teacher.birth_date}
                E-mail - \t{last_created_teacher.email}
                phone - \t{last_created_teacher.phone}
                address - \t{last_created_teacher.address}'''
                )
            )
