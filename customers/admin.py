from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','id','mobile_number','job','image','blood_group')
    search_fields = ('name', 'job')
    ordering = ("-date_added",)