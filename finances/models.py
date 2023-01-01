from django.db import models

from general.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    organized_date = models.DateField(auto_now_add=True,editable=True)
    organizer = models.ForeignKey("members.Member",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "finances_category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name","-date_added")


class Income(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True,on_delete=models.CASCADE)
    initiated_by = models.ForeignKey("members.Member",on_delete=models.CASCADE)
    reciept = models.ImageField(upload_to="finances/reciepts/", null=True, blank=True)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "finances_income"
        verbose_name = "Income"
        verbose_name_plural = "Income"
        ordering = ("title","-date_added")


class Expense(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True,on_delete=models.CASCADE)
    initiated_by = models.ForeignKey("members.Member",on_delete=models.CASCADE)
    reciept = models.ImageField(upload_to="finances/reciepts/", null=True, blank=True)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "finances_expense"
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
        ordering = ("title","-date_added")


class MembershipFee(BaseModel):
    customer = models.ForeignKey("customers.Customer",on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=40)

    def __str__(self):
        return self.customer.name 

    class Meta:
        db_table = "finances_membership_fee"
        verbose_name = "Membership Fee"
        verbose_name_plural = "Membership Fees"
        ordering = ("-date_added",)