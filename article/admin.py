# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article



admin.site.register(Article, ArticleAdmin)
