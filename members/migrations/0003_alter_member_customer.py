# Generated by Django 4.1.4 on 2022-12-15 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('members', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='customers.customer'),
        ),
    ]
