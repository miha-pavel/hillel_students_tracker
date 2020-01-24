import random

from django.core.management.base import BaseCommand

from students.models import Student, Group
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generates 100 random student'

    def add_arguments(self, parser):
        parser.add_argument('--students_count',
                            help='Count of students')
        parser.add_argument('--groups_count',
                            help='Count of groups')

    def handle(self, *args, **options):
        students_count = int(options.get('students_count') or 20)
        groups = [
            Group.create_group()
            for i in range(int(options.get('groups_count') or 10))]
        for i in range(students_count):
            student = Student.generate_person()
            student.group = random.choice(groups)
            student.save()
        count_created_groups = 0
        for group in groups:
            group_students = Student.objects.filter(group=group.id)
            if group_students:
                if not group.head_student:
                    group.head_student = random.choice(group_students)
                if not group.head_teacher:
                    group.head_teacher = Teacher.generate_person()
                group.save()
                count_created_groups += 1
            else:
                Group.objects.get(id=group.id).delete()

        self.stdout.write(
            self.style.SUCCESS(
                f'''Successfully created {count_created_groups} groups and {students_count} random students'''
                )
            )
