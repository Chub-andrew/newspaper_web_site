# Generated by Django 5.0.6 on 2024-05-17 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='year_of_experience',
        ),
    ]
