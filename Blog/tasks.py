from django.apps import apps

from BlogProject.celery import app


@app.task
def publish_task(model_name, object_ids):
	model = apps.get_model('Blog', model_name)
	objs = model.objects.filter(id__in=object_ids, is_published=False, is_deleted=False)
	objs.update(is_published=True)


@app.task
def delete_task(model_name, object_ids):
	model = apps.get_model('Blog', model_name)
	objs = model.objects.filter(id__in=object_ids, is_deleted=False)
	objs.update(is_deleted=True, is_published=False)


@app.task
def include_task(model_name, object_ids):
	model = apps.get_model('Blog', model_name)
	objs = model.objects.filter(id__in=object_ids, is_deleted=True)
	objs.update(is_deleted=False)
