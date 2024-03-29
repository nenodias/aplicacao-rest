# *-* coding:utf-8 *-*
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=5000)
    data_publicacao = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.titulo

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=5000)
    data_publicacao = models.DateTimeField(default=timezone.now, blank=True)
    posts = models.ManyToManyField('Post', related_name='Posts')


    def __str__(self):
        return self.titulo

