from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        abstract = True


class LikableModel(models.Model):
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.dislikes += 1
        self.save()


class Post(BaseModel, LikableModel):
    title = models.CharField(max_length=25, unique=True)
    content = models.TextField()
    category = models.ManyToManyField('Category')
    author = models.ForeignKey(User, models.PROTECT)
    previous_post = models.OneToOneField('self', models.PROTECT, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.title}'


class Category(BaseModel):
    title = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Categories'


class Comment(BaseModel, LikableModel):
    post = models.ForeignKey('Post', models.PROTECT)
    author = models.CharField(max_length=30)
    content = models.TextField()
    previous_comment = models.OneToOneField('self', models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.content}'
