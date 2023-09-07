from Blog.tasks import *


def delete(modeladmin, request, queryset):
	ids = list(queryset.values_list('id', flat=True))
	delete_task.delay(ids)


def publish(modeladmin, request, queryset):
	ids = list(queryset.values_list('id', flat=True))
	publish_task.delay(ids)


delete.short_description = 'Delete Selected'
publish.short_description = 'Publish Selected'
