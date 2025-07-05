from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# English views
urlpatterns = [
    path('', views.home_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('contact/', views.contact_view, name='contact'),
]
