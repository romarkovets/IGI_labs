# Generated by Django 5.0.6 on 2024-11-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='heading',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]