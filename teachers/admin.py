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
    readonly_fields = ('email',)
    # list_select_related = ('group',)

    list_display = ('id', 'first_name', 'last_name', 'email')
    list_display_links = ('last_name',)

    list_per_page = 20
    search_fields = ['^last_name']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('email')
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False
