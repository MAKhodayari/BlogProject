from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from rest_framework import viewsets

from Blog.forms import *
from Blog.serializers import *


class IndexView(TemplateView):
	template_name = 'index.html'
	extra_context = {'title': 'Home', 'message': 'Welcome', 'owner': 'Mohammad Ali Khodayari'}


class UserSignUpView(CreateView):
	form_class = UserSignUpForm
	template_name = 'create_user.html'
	success_url = reverse_lazy('create_post')
	extra_context = {'title': 'Sign Up'}


class UserSignInView(LoginView):
	template_name = 'login.html'
	next_page = reverse_lazy('create_post')
	extra_context = {'title': 'Sign In'}


class UserChangePasswordView(PasswordChangeView):
	template_name = 'change_password.html'


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
	extra_context = {'title': 'Tags', 'header': 'Tag List'}


class TagDetailView(DetailView):
	queryset = Tag.objects.get_published()
	template_name = 'tag_detail.html'


class AuthorListView(ListView):
	queryset = User.objects.all()
	template_name = 'author_list.html'
	extra_context = {'title': 'Authors', 'header': 'Author List'}


class AuthorDetailView(DetailView):
	queryset = User.objects.all()
	template_name = 'author_detail.html'

	def get_object(self, queryset=None):
		return User.objects.get(username=self.kwargs['username'])


class CreatePostView(LoginRequiredMixin, CreateView):
	form_class = PostForm
	template_name = 'create_post.html'
	success_url = reverse_lazy('post_list')
	extra_context = {'title': 'Add Post'}

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


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
