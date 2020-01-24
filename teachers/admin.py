from django.contrib import admin

from .models import (Teacher)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name'), 'birth_date', 'address')
        }),
        ('Connection', {
            'classes': ('collapse',),
            'fields': ('email', 'phone'),
        }),
    )
    readonly_fields = ('email', 'phone')

    list_display = ('id', 'first_name', 'last_name', 'email')
    list_display_links = ('last_name',)
    
    list_per_page = 20
    search_fields = ['^last_name']
