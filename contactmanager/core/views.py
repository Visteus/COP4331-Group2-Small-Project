from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import users

# Handle login request
def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('core:index'))
		else:
			return render(request, 'core/login.html', {
				'error_message': "You are not logged in. Please log in!"
			})
	return render(request, 'core/login.html')


@login_required(login_url='')
def logout_view(request):
	logout(request)
	return render(request, 'core/logout.html')
	

# Contact - main page
@login_required(login_url='')
def index(request):
	return render(request, 'core/contact.html')

# @login_required(login_url='')
# def create_contact(request):



