from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Usuario(AbstractUser):
    class Meta:
            db_table = 'auth_user'

class Post(models.Model):
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Título',max_length=200)
    body = models.TextField(verbose_name='Conteúdo')
    cover = models.ImageField(verbose_name='Imagem', upload_to= 'uploads/', default="DEFAULT VALUE")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
