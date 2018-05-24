from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This message in core/views.py<h1>")