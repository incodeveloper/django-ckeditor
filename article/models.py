# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Article(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title')
    text=CKEditor5Field('Text', config_name='extends')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
