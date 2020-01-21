import random

from django.core.management.base import BaseCommand

from students.models import Student, Group
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates 100 random student'

    def add_arguments(self, parser):
        parser.add_argument('--count',
                            help='Count of items')
        parser.add_argument('--should_create',
                            help='Command should create "students" or "teachers"')

    def handle(self, *args, **options):
        count = int(options.get('count') or 100)
        should_create = options.get('should_create') or 'students'
        groups = [Group.create_group() for i in range(10)]
        for i in range(count):
            if should_create == 'students':
                student = Student.generate_person()
                student.group = random.choice(groups)
            elif should_create == 'teachers':
                teacher = Teacher.generate_person()
                teacher.group = random.choice(groups)

        self.stdout.write(
            self.style.SUCCESS(
                f'''Successfully created {count} random {should_create}'''
                )
            )
