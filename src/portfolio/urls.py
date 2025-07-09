from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
] 