from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import users, contacts
from django.template.context_processors import request

# Handle login request
def login(request):
    return render(request, 'core/login.html')

# Handle core page (Homepage?)
def index(request):
    return HttpResponse("<h1>Homepage maybe? content in core/views.py<h1>")

# Handle delete contact
def delete_contact(request)
	if request.method == 'POST':
		cont_id = request.POST.get('contact_id')	# gets the requested contact's ID
		user = users.objects.get(id = request.user)	# get the user object for the current user
		user.contacts.filter(id = cont_id).delete()	# delete the requested contact from the user's list
	return
