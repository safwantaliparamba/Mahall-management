# Generated by Django 4.1.4 on 2022-12-15 06:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('organized_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'finances_category',
                'ordering': ('name', '-date_added'),
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('reciept', models.ImageField(blank=True, null=True, upload_to='finances/reciepts/')),
                ('amount', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
                'db_table': 'finances_expense',
                'ordering': ('title', '-date_added'),
            },
        ),
        migrations.CreateModel(
            name='MembershipFee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField(default=40)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
            options={
                'verbose_name': 'Membership Fee',
                'verbose_name_plural': 'Membership Fees',
                'db_table': 'finances_membership_fee',
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('reciept', models.ImageField(blank=True, null=True, upload_to='finances/reciepts/')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finances.category')),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Income',
                'db_table': 'finances_income',
                'ordering': ('title', '-date_added'),
            },
        ),
    ]
