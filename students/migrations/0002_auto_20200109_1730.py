# Generated by Django 2.2.9 on 2020-01-09 17:30

from django.db import migrations
import re

def forward(apps, schema_editor):
    pass
    # '''
    # We can't import the Post model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    # '''
    Student = apps.get_model('students', 'Student')
    for student in Student.objects.all().only('id', 'phone').iterator(): #iterator-загружает базу не всю а по частям, only - берем только два поля
        student.phone = ''.join(x for x in student.phone if x.isdigit())
    #     post.slug = slugify(post.title)
        student.save(update_fields=['phone']) # обновляем только номер телефона не всю таблицу


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward),
    ]
