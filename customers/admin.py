from django.contrib import admin

from customers.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','id','mobile_number','job','image','blood_group')
    search_fields = ('name', 'job')

admin.site.register(Customer,CustomerAdmin)