from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name","designation","age","mobile_number","image","salary")
    search_fields = ("name","designation")

