from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    #query to database

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
        }
    )