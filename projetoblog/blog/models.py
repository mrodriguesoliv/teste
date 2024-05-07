#type: ignore
#apenas testando
from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_summernote.models import AbstractAttachment
from utils.image import resized_image
from utils.rands import slugify_new


class PublishPost(AbstractAttachment):
	def save(self, *args, **kwargs):
		if not self.name:
			self.name = self.title.name

		current_file_name = str(self.file.name)
		super_save = super().save(*args, **kwargs)
		file_changed = False

		if self.file:
			file_changed = current_file_name != self.file.name

		if file_changed:
			resized_image(self.file, 900, True, 70)

		return super_save
		
		
class Page(models.Model):
	title = models.CharField(max_length=65,)
	body = models.TextField()

	def save(self, *args, **kwargs):
		return super().save(*args, **kwargs)

	def __str__(self):
		return super().__str__()


class PostManager(models.Manager):
	def get_published(self):
			return self\
					.filter(is_published=True)\
					.order_by('-pk')
  
  
class Post(models.Model):

	objects = PostManager()

	title = models.CharField(max_length=65)
	short_description = models.CharField(max_length=65)
	body = models.TextField()
	cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
	cover_in_post_body = models.BooleanField(
		default=True,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		blank=True,
		null=True,
		related_name='post_created_by'
	)

def __str__(self):
	return self.title

def save(self, *args, **kwargs):
	current_cover_name = str(self.cover.name)
	super_save = super().save(*args, **kwargs)
	cover_changed = False

	if self.cover:
		cover_changed = current_cover_name != self.cover.name

	if cover_changed:
		resized_image(self.cover, 900, True,70)

	return super_save
	 