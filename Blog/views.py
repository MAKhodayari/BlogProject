from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from Blog.models import Post, Category


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Index', 'message': 'Welcome', 'owner': 'Mohammad Ali Khodayari'}


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'post_list.html'
    extra_context = {'title': 'Posts', 'header': 'Post List'}


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'post_detail.html'


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'category_list.html'
    extra_context = {'title': 'Categories', 'header': 'Category List'}


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    template_name = 'category_detail.html'
