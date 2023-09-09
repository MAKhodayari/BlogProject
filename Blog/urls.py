from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Blog.views import *

urlpatterns = [
	# Normal Views
	path('', IndexView.as_view(), name='index'),
	path('posts/', PostListView.as_view(), name='post_list'),
	path('posts/<slug>/', PostDetailView.as_view(), name='post_detail'),
	path('posts/<slug>/like/', ReactToPostView.as_view(reaction='like'), name='like_post'),
	path('posts/<slug>/dislike/', ReactToPostView.as_view(reaction='dislike'), name='dislike_post'),
	path('comments/<pk>/like/', ReactToCommentView.as_view(reaction='like'), name='like_comment'),
	path('comments/<pk>/dislike/', ReactToCommentView.as_view(reaction='dislike'), name='dislike_comment'),
	path('categories/', CategoryListView.as_view(), name='category_list'),
	path('categories/<slug>/', CategoryDetailView.as_view(), name='category_detail'),
	path('tags/', TagListView.as_view(), name='tag_list'),
	path('tags/<slug>/', TagDetailView.as_view(), name='tag_detail'),

	# Authentication Views
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

	# Swagger Views
	path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
	path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
	path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

router = DefaultRouter()
router.register('api/posts', PostViewSet)
router.register('api/categories', CategoryViewSet)
router.register('api/tags', TagViewSet)
router.register('api/comments', CommentViewSet)

urlpatterns += router.urls
