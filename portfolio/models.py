# portfolio/models.py
from django.db import models
from PIL import Image

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()
    image = models.ImageField(upload_to='project_images/')
    custom_content = models.TextField(blank=True)  # Add a new field for custom content

    def __str__(self):
        return self.title



class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='')  # Manually define a default value, for example, an empty string
    message = models.TextField(null=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submission_date}"