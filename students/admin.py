from django.contrib import admin

from .models import (Student, Group)


class GroupInline(admin.TabularInline):
    model = Group
    classes = ['collapse']
    extra = 1


class StudentInline(admin.TabularInline):
    model = Student
    classes = ['collapse']
    extra = 1
    raw_id_fields = ("group",)
    exclude = ('email', 'phone')
    show_change_link = True


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name'), 'birth_date', 'address', 'group')
        }),
        ('Connection', {
            'classes': ('collapse',),
            'fields': ('email', 'phone'),
        }),
    )

    readonly_fields = ('email',)
    list_select_related = ('group',)

    list_display = ('id', 'first_name', 'last_name', 'email')
    list_display_links = ('last_name',)

    list_per_page = 20
    search_fields = ['^last_name']

    inlines = [
        GroupInline,
    ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('email')
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False

    def get_inline_instances(self, request, obj=None):
        return [inline(self.model, self.admin_site) for inline in self.inlines]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide MyInline in the add view
            if isinstance(inline, GroupInline) and obj is None:
                continue
            yield inline.get_formset(request, obj), inline


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('number', 'created_year')
        }),
        ('Department', {
            'classes': ('collapse',),
            'fields': ('department', 'specialty_number', 'specialty_name'),
        }),
        ('Headers', {
            'classes': ('collapse',),
            'fields': ('head_student', 'head_teacher'),
        }),
    )
    list_filter = ['department']
    list_display = ('number', 'head_student', 'head_teacher')
    list_per_page = 20
    search_fields = ['^number' '^created_year' '^department' '^specialty_number' '^specialty_name']

    inlines = [
        StudentInline,
    ]
