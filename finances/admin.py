from django.contrib import admin

from finances.models import Category, Income, Expense, MembershipFee


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","id","organized_date","organizer")
    search_fields = ("name","organizer")


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("title","id","category","initiated_by","amount","reciept")
    search_fields = ("title","category","initiated_by","amount")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title","id","category","initiated_by","amount","reciept")
    search_fields = ("title","category","initiated_by","amount")


@admin.register(MembershipFee)
class MembershipFeeAdmin(admin.ModelAdmin):
    list_display = ("customer","amount","date_added")
    search_fields = ("customer","amount")


