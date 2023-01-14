#from django.shortcuts import render
from .models import Post, Category

from django.views.generic import ListView, DetailView
# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     #query to database
#     # post 를 가져와라.
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self,**kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context