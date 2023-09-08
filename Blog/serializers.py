from rest_framework import serializers

from Blog.models import *


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['id', 'post', 'author', 'content', 'previous_comment']


class PostSerializer(serializers.ModelSerializer):
	comment_set = CommentSerializer(many=True, read_only=True)

	class Meta:
		model = Post
		fields = [
			'id', 'title', 'content', 'author', 'category', 'previous_post', 'slug', 'likes', 'dislikes', 'views',
			'comment_set']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'title', 'slug']
