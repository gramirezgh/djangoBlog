# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=120)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

    def get_absolute(self):
        return reverse("solo", kwarg={"id":self.id,"slug":self.slug})