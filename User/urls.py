from django.contrib.auth.views import LogoutView
from django.urls import path

from User.views import *

urlpatterns = [
	path('signup/', UserSignUpView.as_view(), name='sign_up'),
	path('signin/', UserSignInView.as_view(), name='sign_in'),
	path('logout/', LogoutView.as_view(), name='log_out'),
	path('change_password/', UserChangePasswordView.as_view(), name='change_password'),
]
