# Generated by Django 5.0.6 on 2024-06-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
        migrations.AddField(
            model_name='employee',
            name='schedule',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='list_of_jobs',
            field=models.CharField(default='', max_length=200),
        ),
    ]