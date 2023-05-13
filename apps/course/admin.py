from django.contrib import admin

from apps.course.models import Department


# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'is_active', 'created_at', 'updated_at')
    ordering = ('name', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Department, DepartmentAdmin)
