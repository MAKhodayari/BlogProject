from Blog.models import Post
from BlogProject.celery import app


@app.task
def delete_post_task(ids):
    posts = Post.objects.filter(id__in=ids)
    for post in posts:
        post.is_deleted = True
        post.save()
