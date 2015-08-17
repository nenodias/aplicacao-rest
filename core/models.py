# *-* coding:utf-8 *-*
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=5000)
    data_publicaco = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.titulo
