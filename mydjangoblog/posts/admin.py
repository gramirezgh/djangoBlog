# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "fecha"]
    list_filter = ["fecha"]
    search_fields = ["titulo", "contenido"]
    prepopulated_fields = {"slug": ("titulo",)}

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)