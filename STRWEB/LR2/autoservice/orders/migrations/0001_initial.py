# Generated by Django 5.0.6 on 2024-06-23 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('users', '0009_customer_alter_employee_list_of_jobs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employee')),
                ('services', models.ManyToManyField(blank=True, to='services.service')),
            ],
        ),
    ]
