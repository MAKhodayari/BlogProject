from Blog.tasks import *


def publish(modeladmin, request, queryset):
	object_ids = list(queryset.values_list('id', flat=True))
	model_name = queryset.model.__name__
	publish_task.delay(model_name, object_ids)


def delete(modeladmin, request, queryset):
	object_ids = list(queryset.values_list('id', flat=True))
	model_name = queryset.model.__name__
	delete_task.delay(model_name, object_ids)


def include(modeladmin, request, queryset):
	object_ids = list(queryset.values_list('id', flat=True))
	model_name = queryset.model.__name__
	include_task.delay(model_name, object_ids)


publish.short_description = 'Publish Selected'
delete.short_description = 'Delete Selected'
include.short_description = 'Include Selected'
