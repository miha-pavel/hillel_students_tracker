from django.core.management.base import BaseCommand

from students.models import Student, Group
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates 100 random student'

    def add_arguments(self, parser):
        parser.add_argument('--count',
                            help='Count of items')
        parser.add_argument('--should_create',
                            help='Command should create "students" or "teachers" or "groups"')

    def handle(self, *args, **options):
        count = int(options.get('count') or 100)
        should_create = options.get('should_create') or 'students'
        i = 1
        while i <= count:
            if should_create == 'students':
                Student.create_person()
            elif should_create == 'teachers':
                Teacher.create_person()
            elif should_create == 'groups':
                Group.create_group()
            i += 1
        self.stdout.write(
            self.style.SUCCESS(
                f'''Successfully created {count} random {should_create}'''
                )
            )
