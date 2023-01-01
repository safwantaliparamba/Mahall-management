from django.contrib import admin

from finances.models import Category, Income, Expense, MembershipFee

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","id","organized_date","organizer")
    search_fields = ("name","organizer")

class IncomeAdmin(admin.ModelAdmin):
    list_display = ("title","id","category","initiated_by","amount","reciept")
    search_fields = ("title","category","initiated_by","amount")

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title","id","category","initiated_by","amount","reciept")
    search_fields = ("title","category","initiated_by","amount")

class MembershipFeeAdmin(admin.ModelAdmin):
    list_display = ("customer","amount","date_added")
    search_fields = ("customer","amount")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(MembershipFee, MembershipFeeAdmin)