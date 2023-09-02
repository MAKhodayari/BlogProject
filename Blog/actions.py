from Blog.tasks import delete_post_task


def delete_post(ModelAdmin, request, queryset):
    ids = list(queryset.values_list('id', flat=True))
    delete_post_task.delay(ids)
