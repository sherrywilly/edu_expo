from django.db import models


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name="Course Name", )
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "Departments"
        verbose_name = "Department"

    def __str__(self):
        return self.name
