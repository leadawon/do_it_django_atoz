#from django.shortcuts import render
from .models import Post

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

# def single_post_page(request,pk):
#     post = Post.objects.get(pk=pk)
#     # query to database
#     # pk에 해당하는 post 를 가져와라.
#
#     return render(
#         request,
#         'blog/post_detail.html', #post record를 html파일에 담아서 랜더링한다.
#         {
#             'post':post,
#         }
#     )

class PostDetail(DetailView):
    model = Post