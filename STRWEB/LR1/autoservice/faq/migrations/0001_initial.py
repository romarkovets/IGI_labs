# Generated by Django 5.0.6 on 2024-06-23 06:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100)),
                ('answer', models.TextField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]