from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets

from Blog.models import *
from Blog.serializers import *


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Home', 'message': 'Welcome', 'owner': 'Mohammad Ali Khodayari'}


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'post_list.html'
    extra_context = {'title': 'Posts', 'header': 'Post List'}


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'post_detail.html'


class ReactToPostView(View):
    reaction = None

    @method_decorator(login_required)
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        if self.reaction == 'like':
            post.like()
        elif self.reaction == 'dislike':
            post.dislike()
        return redirect('post_detail', slug=post.slug)


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'category_list.html'
    extra_context = {'title': 'Categories', 'header': 'Category List'}


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    template_name = 'category_detail.html'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
