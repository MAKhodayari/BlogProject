from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=25, unique=True)
    content = models.TextField()
    category = models.ManyToManyField('Category')
    author = models.ForeignKey(User, models.PROTECT)
    previous_post = models.OneToOneField('self', models.PROTECT, null=True, blank=True)
    slug = models.SlugField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)


class Category(BaseModel):
    title = models.CharField(max_length=15, unique=True)
    slug = models.SlugField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name_plural = 'Categories'


class Comment(BaseModel):
    author = models.CharField(max_length=30)
    content = models.TextField()
    post = models.ForeignKey('Post', models.PROTECT)
