# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def site_index(request):
    return HttpResponse("Hello!")
