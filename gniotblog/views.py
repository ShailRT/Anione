from django.shortcuts import render, get_object_or_404
from post.models import Post

def home(request):
    recent_post = Post.objects.all()[:3]
    return render(request, 'index.html', {'posts': recent_post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
