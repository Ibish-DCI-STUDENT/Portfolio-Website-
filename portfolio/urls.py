# portfolio/urls.py
from django.urls import path
from .views import home, about, projects, project_detail, contact ,contact_success 

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('project/<int:project_id>/', project_detail, name='project_detail'), 
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),

]
