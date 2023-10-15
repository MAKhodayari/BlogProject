from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from User.forms import UserSignUpForm


class UserSignUpView(CreateView):
	form_class = UserSignUpForm
	template_name = 'User/create_user.html'
	success_url = reverse_lazy('post_create')
	extra_context = {'title': 'Sign Up'}


class UserSignInView(LoginView):
	template_name = 'User/login.html'
	next_page = reverse_lazy('post_create')
	extra_context = {'title': 'Sign In'}


class UserChangePasswordView(PasswordChangeView):
	template_name = 'Blog/change_password.html'
