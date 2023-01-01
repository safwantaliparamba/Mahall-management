from django.contrib import admin

from members.models import Member  


class MemberAdmin(admin.ModelAdmin):
    list_display = ("name","position","department","customer","user","id")
    search_fields = ("name","position","department","user")
    exclude = ("encrypted_password",)

admin.site.register(Member,MemberAdmin)