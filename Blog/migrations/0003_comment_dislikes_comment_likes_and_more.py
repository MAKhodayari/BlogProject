# Generated by Django 4.2.4 on 2023-09-04 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
	dependencies = [
		('Blog', '0002_alter_category_slug_alter_post_slug'),
	]

	operations = [
		migrations.AddField(
			model_name='comment',
			name='dislikes',
			field=models.PositiveIntegerField(default=0),
		),
		migrations.AddField(
			model_name='comment',
			name='likes',
			field=models.PositiveIntegerField(default=0),
		),
		migrations.AddField(
			model_name='comment',
			name='previous_comment',
			field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
									   to='Blog.comment'),
		),
		migrations.AddField(
			model_name='post',
			name='dislikes',
			field=models.PositiveIntegerField(default=0),
		),
		migrations.AddField(
			model_name='post',
			name='likes',
			field=models.PositiveIntegerField(default=0),
		),
		migrations.AlterField(
			model_name='category',
			name='is_published',
			field=models.BooleanField(default=False),
		),
		migrations.AlterField(
			model_name='comment',
			name='is_published',
			field=models.BooleanField(default=False),
		),
		migrations.AlterField(
			model_name='post',
			name='is_published',
			field=models.BooleanField(default=False),
		),
	]
