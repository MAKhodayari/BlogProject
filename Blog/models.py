from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatewords
from django.utils.text import slugify


class BaseManager(models.Manager):

	def get_all(self):
		return super().get_queryset()

	def get_published(self):
		return super().get_queryset().filter(is_published=True)


class BaseModel(models.Model):
	objects = BaseManager()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_deleted = models.BooleanField(default=False)
	is_published = models.BooleanField(default=False)

	class Meta:
		abstract = True


class IntractableModel(models.Model):
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


class Post(BaseModel, IntractableModel):
	title = models.CharField(max_length=25, unique=True)
	content = models.TextField()
	category = models.ManyToManyField('Category', related_name='posts')
	tag = models.ManyToManyField('Tag', related_name='posts')
	author = models.ForeignKey(User, models.PROTECT, related_name='posts')
	parent_post = models.OneToOneField('self', models.PROTECT, related_name='posts', null=True, blank=True)
	slug = models.SlugField(unique=True)
	views = models.PositiveIntegerField(default=0)

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.slug = slugify(self.title)
		super().save(force_insert, force_update, using, update_fields)

	def increment_view(self):
		self.views += 1
		self.save()

	def __str__(self):
		return f'{self.title}'


class Category(BaseModel):
	title = models.CharField(max_length=15, unique=True)
	slug = models.SlugField(unique=True)
	parent_category = models.ForeignKey('self', models.PROTECT, related_name='categories', null=True, blank=True)

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.slug = slugify(self.title)
		super().save(force_insert, force_update, using, update_fields)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name_plural = 'Categories'


class Tag(BaseModel):
	title = models.CharField(max_length=15, unique=True)
	slug = models.SlugField(unique=True)

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.slug = slugify(self.title)
		super().save(force_insert, force_update, using, update_fields)

	def __str__(self):
		return f'{self.title}'


class Comment(BaseModel, IntractableModel):
	post = models.ForeignKey('Post', models.PROTECT, related_name='comments')
	author = models.CharField(max_length=30)
	content = models.TextField()
	parent_comment = models.ForeignKey('self', models.PROTECT, related_name='comments', null=True, blank=True)

	def __str__(self):
		return f'{truncatewords(self.content, 15)}'
