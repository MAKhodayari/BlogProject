from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from User.forms import UserSignUpForm


class UserSignUpView(CreateView):
	form_class = UserSignUpForm
	template_name = 'User/signup.html'
	success_url = reverse_lazy('post_create')
	extra_context = {'title': 'Sign Up'}


class UserLogInView(LoginView):
	template_name = 'User/login.html'
	next_page = reverse_lazy('post_create')
	extra_context = {'title': 'Sign In'}


class UserLogOutView(LogoutView):
	template_name = 'User/logout.html'
	extra_context = {'title': 'Log Out'}


class UserPasswordChangeView(PasswordChangeView):
	template_name = 'Blog/../templates/User/change_password.html'
	extra_context = {'title': 'Change Password'}
