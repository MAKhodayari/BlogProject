from django.urls import path
from rest_framework.routers import DefaultRouter

from Blog.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug>/', CategoryDetailView.as_view(), name='category_detail')
]

router = DefaultRouter()
router.register('api/posts', PostViewSet)
router.register('api/categories', CategoryViewSet)
router.register('api/comments', CommentViewSet)

urlpatterns += router.urls