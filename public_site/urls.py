from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# English views
urlpatterns = [
    path('', views.home_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<int:category_id>/', views.category_view, name='category'),
    path('contact/', views.contact_view, name='contact'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions_view, name='terms_and_conditions'),
    path('blog/', views.blog_list_view, name='blog_list'),
    path('blog/<int:post_id>/', views.blog_detail_view, name='blog_detail'),
]
