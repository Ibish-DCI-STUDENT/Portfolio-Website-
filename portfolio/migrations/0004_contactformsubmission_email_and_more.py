# Generated by Django 5.0.1 on 2024-01-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0003_contactformsubmission"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactformsubmission",
            name="email",
            field=models.EmailField(default="", max_length=254),
        ),
        migrations.AddField(
            model_name="contactformsubmission",
            name="message",
            field=models.TextField(null=True),
        ),
    ]
