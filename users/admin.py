from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','id','email')
    search_fields = ('username','email')
    exclude = ('password',)

admin.site.register(User,UserAdmin)