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
		
class Page(models.Model):
	title = models.CharField(max_length=65,)
	body = models.TextField()

	def save(self, *args, **kwargs):
		return super().save(*args, **kwargs)

	def __str__(self):
		return super().__str__()
  
