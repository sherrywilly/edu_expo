from django.db import models

from apps.course.models import Department
from apps.school.models import School


class Stream(models.Model):
    name = models.CharField(max_length=200, verbose_name="Stream Name", )
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "stream"
        verbose_name = "Stream"

    def __str__(self):
        return self.name


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name", )
    mobile_number = models.CharField(max_length=10, verbose_name="Mobile Number", unique=True)
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField(max_length=100, verbose_name="Email")
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="School",
                               related_name="school")
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, verbose_name="Stream", related_name="stream")
    interested_course = models.ForeignKey(Department, on_delete=models.CASCADE,
                                          verbose_name="Interested Course",
                                          related_name="department")
    funding_type = models.CharField(max_length=100, verbose_name="Funding Type", choices=(
        ("EDUCATION_LOAN", "Education Loan"),
        ("SELF_FINANCE", "Self Finance"),
    ), default="SELF_FINANCE")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Student"


class StudentCertificates(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student",
                                related_name="student_certificates")
    sslc = models.FileField(upload_to='student_certificates', verbose_name="SSLC")
    plus_two = models.FileField(upload_to='student_certificates', verbose_name="Plus Two")
    plus_one = models.FileField(upload_to='student_certificates', verbose_name="Plus One")

    class Meta:
        verbose_name = "Student Certificates"
