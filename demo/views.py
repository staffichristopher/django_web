# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><head><title>StaffiChristopher Website</title></head><body><h1>Hello, StaffiChristopher 😀</h1></body></html>") 