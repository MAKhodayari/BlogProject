from django.urls import path

from Blog.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug>/', CategoryDetailView.as_view(), name='category_detail')
]
