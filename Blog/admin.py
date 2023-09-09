from django.contrib import admin
from django.template.defaultfilters import truncatechars

from Blog.actions import *
from Blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'content', 'category', 'tag', 'author', 'previous_post']
	list_display = [
		'title', 'shorten_content', 'get_categories', 'get_tags', 'author', 'previous_post', 'likes', 'dislikes',
		'get_comment_count', 'views', 'is_deleted', 'is_published'
	]
	list_filter = ['category', 'is_deleted', 'is_published']
	search_fields = ['title', 'content', 'author__username']
	ordering = ['-created_at']
	actions = [delete, include, publish]
	list_per_page = 10

	def shorten_content(self, obj):
		return truncatechars(obj.content, 26)

	shorten_content.short_description = 'content'

	def get_categories(self, obj):
		return ', '.join([c.title for c in obj.category.all()])

	get_categories.short_description = 'categories'

	def get_tags(self, obj):
		return ', '.join([t.title for t in obj.tag.all()])

	get_tags.short_description = 'tags'

	def get_comment_count(self, obj):
		return obj.comment_set.count()

	get_comment_count.short_description = 'comment count'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	fields = ['title']
	list_display = ['title', 'get_post_count', 'is_deleted', 'is_published']
	ordering = ['title']
	actions = [delete, include, publish]

	def get_post_count(self, obj):
		return obj.post_set.count()

	get_post_count.short_description = 'post count'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	fields = ['title']
	list_display = ['title', 'get_post_count', 'is_deleted', 'is_published']
	ordering = ['title']
	actions = [delete, include, publish]

	def get_post_count(self, obj):
		return obj.post_set.count()

	get_post_count.short_description = 'post count'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	fields = ['author', 'content', 'post', 'previous_comment']
	list_display = [
		'author', 'shorten_content', 'post', 'shorten_comment', 'likes', 'dislikes', 'is_deleted', 'is_published'
	]
	search_fields = ['author', 'content', 'post__title']
	ordering = ['-post__title', '-created_at']
	actions = [delete, include, publish]
	list_per_page = 10

	def shorten_content(self, obj):
		return truncatechars(obj.content, 26)

	shorten_content.short_description = 'content'

	def shorten_comment(self, obj):
		if obj.previous_comment is not None:
			return truncatechars(obj.previous_comment, 26)
		else:
			return

	shorten_comment.short_description = 'previous comment'
