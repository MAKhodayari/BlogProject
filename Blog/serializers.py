from rest_framework import serializers

from Blog.models import *


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['id', 'post', 'author', 'content', 'previous_comment', 'likes', 'dislikes']

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		if representation['previous_comment'] is None:
			representation.pop('previous_comment')
		return representation


class CommentNestedSerializer(CommentSerializer, serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['author', 'content', 'previous_comment', 'likes', 'dislikes']


class PostSerializer(serializers.ModelSerializer):
	comment_set = CommentNestedSerializer(many=True, read_only=True)
	author = serializers.SlugRelatedField('username', read_only=True)
	category = serializers.SlugRelatedField('title', many=True, read_only=True)
	tag = serializers.SlugRelatedField('title', many=True, read_only=True)
	previous_post = serializers.SlugRelatedField('id', read_only=True)

	class Meta:
		model = Post
		fields = [
			'id', 'title', 'content', 'author', 'category', 'tag', 'previous_post', 'slug', 'likes', 'dislikes',
			'views', 'comment_set'
		]

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		if representation['previous_post'] is None:
			representation.pop('previous_post')
		if not representation['comment_set']:
			representation.pop('comment_set')
		return representation


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'title', 'slug']


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ['id', 'title', 'slug']
