from django.contrib import admin
from django.db.models import Count

from Blog.actions import *
from Blog.models import *

admin.site.disable_action('delete_selected')


class BaseAdmin(admin.ModelAdmin):
	list_display = ['is_deleted', 'is_published']
	list_filter = ['is_deleted', 'is_published']
	actions = [delete, include, publish]
	list_per_page = 10


@admin.register(Post)
class PostAdmin(BaseAdmin):
	fields = ['title', 'content', 'category', 'tag', 'author', 'parent_post']
	list_display = [
		'shorten_title', 'shorten_content', 'get_category', 'get_tag', 'author', 'shorten_post', 'likes', 'dislikes',
		'get_comment_count', 'views'
	] + BaseAdmin.list_display
	list_filter = ['category', 'tag'] + BaseAdmin.list_filter
	search_fields = ['title', 'content', 'author__username']
	ordering = ['-created_at']

	def get_queryset(self, request):
		queryset = super().get_queryset(request)
		queryset = queryset.annotate(comment_count=Count('comments'))
		return queryset

	def shorten_title(self, obj):
		return truncatewords(obj.title, 10)

	def shorten_content(self, obj):
		return truncatewords(obj.content, 15)

	def shorten_post(self, obj):
		if obj.parent_post is not None:
			return truncatewords(obj.parent_post.title, 10)
		return

	def get_category(self, obj):
		return ', '.join([c.title for c in obj.category.all()])

	def get_tag(self, obj):
		return ', '.join([t.title for t in obj.tag.all()])

	def get_comment_count(self, obj):
		return obj.comment_count

	shorten_title.short_description = 'title'
	shorten_content.short_description = 'content'
	shorten_post.short_description = 'parent_post'
	get_category.short_description = 'category'
	get_tag.short_description = 'tag'
	get_comment_count.short_description = 'comment count'


@admin.register(Comment)
class CommentAdmin(BaseAdmin):
	fields = ['author', 'content', 'post', 'parent_comment']
	list_display = [
		'author', 'shorten_content', 'shorten_post', 'shorten_comment', 'likes', 'dislikes'
	] + BaseAdmin.list_display
	search_fields = ['author', 'content', 'post__title']
	ordering = ['-post__title', '-created_at']

	def shorten_content(self, obj):
		return truncatewords(obj.content, 15)

	def shorten_post(self, obj):
		return truncatewords(obj.post.title, 10)

	def shorten_comment(self, obj):
		if obj.parent_comment is not None:
			return truncatewords(obj.parent_comment, 10)
		return

	shorten_content.short_description = 'content'
	shorten_post.short_description = 'post'
	shorten_comment.short_description = 'parent comment'


@admin.register(Tag)
class TagAdmin(BaseAdmin):
	fields = ['title']
	list_display = ['title', 'get_post_count'] + BaseAdmin.list_display
	ordering = ['title']

	def get_queryset(self, request):
		queryset = super().get_queryset(request)
		queryset = queryset.annotate(post_count=Count('posts'))
		return queryset

	def get_post_count(self, obj):
		return obj.post_count

	get_post_count.short_description = 'post count'


@admin.register(Category)
class CategoryAdmin(TagAdmin):
	fields = TagAdmin.fields + ['parent_category']
