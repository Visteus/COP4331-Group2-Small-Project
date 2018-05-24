from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import users
from django.template.context_processors import request

# Handle login request
def login(request):
    return render(request, 'core/login.html')

# Handle core page (Homepage?)
def index(request):
    return HttpResponse("<h1>Homepage maybe? content in core/views.py<h1>")
