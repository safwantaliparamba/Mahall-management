from django.contrib import admin

from houses.models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_number','id','name','address','mobile_number')
    search_fields = ('house_number','name','address')

admin.site.register(House,HouseAdmin)