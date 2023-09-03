from django.contrib import admin
from django.template.defaultfilters import truncatechars

from Blog.actions import *
from Blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'category', 'author', 'previous_post']
    list_display = [
        'title', 'shorten_content', 'get_categories', 'author', 'previous_post', 'slug', 'is_deleted', 'is_published'
    ]
    list_filter = ['category', 'is_deleted', 'is_published']
    search_fields = ['title', 'content', 'author__username', 'category__title']
    ordering = ['title', 'author']
    actions = [delete, publish]
    list_per_page = 10

    def shorten_content(self, obj):
        return truncatechars(obj.content, 11)
    shorten_content.short_description = 'content'

    def get_categories(self, obj):
        return ', '.join([c.title for c in obj.category.all()])
    get_categories.short_description = 'categories'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ['title', 'slug', 'is_deleted', 'is_published']
    ordering = ['title']
    actions = [delete, publish]
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'content', 'post']
    list_display = ['author', 'content', 'post', 'is_deleted', 'is_published']
    search_fields = ['author', 'content', 'post__title']
    ordering = ['post__title', 'author']
    actions = [delete, publish]
    list_per_page = 10
