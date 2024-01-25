# portfolio/forms.py
from django import forms
from .models import ContactFormSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ['name', 'email', 'message']
        
        

""" Used Django's built-in ModelForm features to simplify the form handling process.
By making ContactForm a subclass of ModelForm and specifying the model in the Meta class,
you can leverage the save method provided by ModelForm to handle the form submission, 
including saving the data to the database.

The save method takes care of creating a new instance of the model and saving it to the database. 
In this case, it's the ContactFormSubmission model.
"""