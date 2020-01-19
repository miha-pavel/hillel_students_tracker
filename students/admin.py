from django.contrib import admin

from .models import (Student, Group)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name'), 'birth_date', 'address')
        }),
        ('Connection', {
            'classes': ('collapse',),
            'fields': ('email', 'phone'),
        }),
    )
    list_display = ('first_name', 'last_name', 'email')
    list_display_links = ('last_name',)
    list_per_page = 20
    search_fields = ['^last_name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('number', 'created_year', 'address')
        }),
        ('Department', {
            'classes': ('collapse',),
            'fields': ('department', 'specialty_number', 'specialty_name'),
        }),
    )
    list_filter = ['department']
    list_display = ('__str__',)
    list_per_page = 20
    search_fields = ['^number' '^created_year' '^department' '^specialty_number' '^specialty_name']
