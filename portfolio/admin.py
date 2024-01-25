# portfolio/admin.py
from django.contrib import admin
from .models import Project
from .models import ContactFormSubmission

admin.site.register(Project)
admin.site.register(ContactFormSubmission)

