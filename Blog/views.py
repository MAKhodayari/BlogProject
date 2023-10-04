from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets

from Blog.serializers import *


class IndexView(TemplateView):
	template_name = 'index.html'
	extra_context = {'title': 'Home', 'message': 'Welcome', 'owner': 'Mohammad Ali Khodayari'}


class PostListView(ListView):
	queryset = Post.objects.get_published()
	template_name = 'post_list.html'
	extra_context = {'title': 'Posts', 'header': 'Post List'}


class PostDetailView(DetailView):
	queryset = Post.objects.get_published()
	template_name = 'post_detail.html'

	def get_object(self, queryset=None):
		obj = super().get_object(queryset)
		obj.increment_view()
		return obj


class ReactToPostView(LoginRequiredMixin, View):
	reaction = None

	def post(self, request, slug):
		post = Post.objects.get(slug=slug)
		if self.reaction == 'like':
			post.like()
		elif self.reaction == 'dislike':
			post.dislike()
		return redirect('post_detail', slug=post.slug)


class ReactToCommentView(LoginRequiredMixin, View):
	reaction = None

	def post(self, request, pk):
		comment = Comment.objects.get(id=pk)
		if self.reaction == 'like':
			comment.like()
		elif self.reaction == 'dislike':
			comment.dislike()
		return redirect('post_detail', slug=comment.post.slug)


class CategoryListView(ListView):
	queryset = Category.objects.get_published()
	template_name = 'category_list.html'
	extra_context = {'title': 'Categories', 'header': 'Category List'}


class CategoryDetailView(DetailView):
	queryset = Category.objects.get_published()
	template_name = 'category_detail.html'


class TagListView(ListView):
	queryset = Tag.objects.get_published()
	template_name = 'tag_list.html'
	extra_context = {'title': 'Categories', 'header': 'Category List'}


class TagDetailView(DetailView):
	queryset = Tag.objects.get_published()
	template_name = 'tag_detail.html'


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.get_published()
	serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.get_published()
	serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.get_published()
	serializer_class = TagSerializer


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.get_published()
	serializer_class = CommentSerializer
