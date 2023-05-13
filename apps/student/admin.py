from django.contrib import admin

from apps.student.models import StudentCertificates, Student, Stream
from apps.student.resources import StudentResource
from import_export.admin import ImportExportMixin,ExportMixin


# Register your models here.


class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


class StudentCertificatesInline(admin.TabularInline):
    model = StudentCertificates
    extra = 1


class StudentAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    list_display = ('name', 'mobile_number', 'date_of_birth', 'email', 'school', 'stream', 'interested_course',
                    'funding_type', 'created_at', 'updated_at')
    list_filter = ('school', 'stream', 'interested_course', 'funding_type',)
    search_fields = ('name', 'mobile_number', 'email')
    ordering = ('name',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    inlines = [StudentCertificatesInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Stream, StreamAdmin)
