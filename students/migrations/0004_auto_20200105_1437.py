# Generated by Django 2.2.9 on 2020-01-05 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200104_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='best_student',
        ),
        migrations.RemoveField(
            model_name='group',
            name='curator',
        ),
        migrations.RemoveField(
            model_name='group',
            name='worst_student',
        ),
    ]