# Generated by Django 5.0.6 on 2024-05-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_remove_author_year_of_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="year_of_experience",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
