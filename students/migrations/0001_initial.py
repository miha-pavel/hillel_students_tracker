# Generated by Django 2.2.9 on 2020-01-21 05:40

from django.db import migrations, models
import students.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('created_year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020)),
                ('department', models.CharField(choices=[('E', 'Electrification'), ('M', 'Mechanics'), ('BT', 'Bridges and tunnels'), ('IT', 'Information Technology')], default='E', max_length=3)),
                ('specialty_number', models.PositiveSmallIntegerField(default=141)),
                ('specialty_name', models.CharField(default='electrition', max_length=255)),
                ('skipped_classes', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('min_rating', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('max_rating', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('standard_deviation_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('mode_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('median_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', students.fields.JSONField()),
                ('message_file', models.FileField(blank=True, null=True, upload_to='messages/')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]
