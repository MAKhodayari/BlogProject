from django.urls import path

from User.views import *

urlpatterns = [
	path('signup/', UserSignUpView.as_view(), name='sign_up'),
	path('signin/', UserLogInView.as_view(), name='sign_in'),
	path('logout/', UserLogOutView.as_view(), name='log_out'),
	path('change_password/', UserPasswordChangeView.as_view(), name='change_password'),
]
