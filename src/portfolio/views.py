from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Project

def home(request):
    return render(request, 'portfolio/under_construction.html')

def blog(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'portfolio/blog.html', {'posts': posts})

def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'portfolio/blog_post.html', {'post': post})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html') 