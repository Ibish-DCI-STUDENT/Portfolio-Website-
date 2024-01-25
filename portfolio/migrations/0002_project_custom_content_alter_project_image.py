# Generated by Django 5.0.1 on 2024-01-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="custom_content",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="project_images/"),
        ),
    ]