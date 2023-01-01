from django.db import models

from general.models import BaseModel


class Employee(BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to="employees/profile/",null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    designation = models.CharField(max_length=128)
    age = models.IntegerField(default=18)
    employee_id = models.CharField(max_length=30)
    salary = models.PositiveIntegerField(default=10000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employees_employee'
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ('name','-salary')