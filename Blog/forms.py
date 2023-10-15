from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Blog.models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'category', 'tag', 'parent_post']


class UserSignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
