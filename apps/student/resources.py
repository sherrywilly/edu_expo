from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from apps.course.models import Department
from apps.school.models import School
from apps.student.models import Student, Stream


class StudentResource(resources.ModelResource):
    school = fields.Field(
        column_name='school',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name')
    )
    stream = fields.Field(
        column_name='stream',
        attribute='stream',
        widget=ForeignKeyWidget(Stream, 'name')
    )
    interested_course = fields.Field(
        column_name='interested_course',
        attribute='interested_course',
        widget=ForeignKeyWidget(Department, 'name')
    )

    class Meta:
        model = Student
        fields = ('id', 'name', 'date_of_birth',
                  'mobile_number',
                  'email', 'school', 'stream', 'interested_course', 'funding_type')
        export_order = (
        'id', 'name', 'date_of_birth', 'mobile_number', 'email', 'school', 'stream', 'interested_course',
        'funding_type')
        import_id_fields = (
            'id', 'name', 'date_of_birth', 'email', 'school', 'stream', 'interested_course', 'funding_type')
        skip_unchanged = True
        report_skipped = True
        dry_run = True
