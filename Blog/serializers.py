from rest_framework import serializers

from Blog.models import *


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['id', 'post', 'author', 'content', 'parent_comment', 'likes', 'dislikes']

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		if representation['parent_comment'] is None:
			representation.pop('parent_comment')
		return representation


class CommentNestedSerializer(CommentSerializer, serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['author', 'content', 'parent_comment', 'likes', 'dislikes']


class PostSerializer(serializers.ModelSerializer):
	comments = CommentNestedSerializer(many=True, read_only=True)
	author = serializers.SlugRelatedField('username', read_only=True)
	category = serializers.SlugRelatedField('title', many=True, read_only=True)
	tag = serializers.SlugRelatedField('title', many=True, read_only=True)
	parent_post = serializers.SlugRelatedField('id', read_only=True)

	class Meta:
		model = Post
		fields = [
			'id', 'title', 'content', 'author', 'category', 'tag', 'parent_post', 'slug', 'likes', 'dislikes',
			'views', 'comments'
		]

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		if representation['parent_post'] is None:
			representation.pop('parent_post')
		if not representation['comments']:
			representation.pop('comments')
		return representation


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'title', 'slug']


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ['id', 'title', 'slug']
