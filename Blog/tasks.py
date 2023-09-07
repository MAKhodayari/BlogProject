from Blog.models import Post
from BlogProject.celery import app


@app.task
def delete_task(ids):
	objs = Post.objects.filter(id__in=ids)
	for obj in objs:
		obj.is_deleted = True
		obj.save()


@app.task
def publish_task(ids):
	objs = Post.objects.filter(id__in=ids)
	for obj in objs:
		obj.is_published = True
		obj.save()
