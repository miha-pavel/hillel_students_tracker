# Generated by Django 2.2.9 on 2020-02-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200127_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('method', models.PositiveSmallIntegerField(choices=[(0, 'GET'), (1, 'POST'), (2, 'DELETE'), (3, 'PUT'), (4, 'PATCH'), (5, 'HEAD'), (6, 'CONNECT'), (7, 'OPTIONS'), (8, 'TRACE')], default=0)),
                ('ime_delta', models.PositiveSmallIntegerField()),
                ('user_id', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Logger',
                'verbose_name_plural': 'Loggers',
            },
        ),
    ]