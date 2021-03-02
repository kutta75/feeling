# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 
            "hello" : "hello"
            }
    return render(request,"eva1/index.html",context)
