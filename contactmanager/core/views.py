from django.shortcuts import render, get_object_or_404, render_to_response
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.db.models import Q

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('core:contact_view'))
		else:
			return render(
				request, 
				'core/login.html', 
				{
					'error_message': "You are not logged in. Please log in!"
				}
			)
	return render(request, 'core/login.html')


def create_new_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		user = User.objects.create_user(
			username=username,
			password=password,
			email=email,
			first_name=first_name,
			last_name=last_name
		)
		user.save()
		return HttpResponseRedirect(reverse('core:login_view'))
	return render(request, 'core/newuser.html')


@login_required(login_url='')
def contact_view(request):
	user_id = request.user.id
	contact_list = Contact.objects.filter(user_id = user_id)
	return render(
		request, 
		'core/contact.html',
		{
			'contact_list': contact_list
		}
	)


@login_required(login_url='')
def create_new_contact(request):
	if request.method == 'POST':
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		email = request.POST['email']
		phone_number = request.POST['phonenumber']
		new_contact = Contact.objects.create(
			first_name=first_name,
			last_name=last_name,
			email=email,
			phone_number=phone_number,
			user=request.user
		)
		new_contact.save()
		return HttpResponseRedirect(reverse('core:contact_view'))
	return render(request, 'core/newcontact.html')


@login_required(login_url='')
def contact_detail_view(request, contact_id):
	contact = get_object_or_404(Contact, pk=contact_id)
	if request.method == 'POST':
		# Delete contact
		if contact.user == request.user:
			if request.POST['delete-contact']:
				contact.delete()
				return HttpResponseRedirect(reverse('core:contact_view'))
	return render(
		request,
		'core/contactdetail.html',
		{
			'contact': contact
		}
	)
		

@login_required(login_url='')
def search_contact(request):
	if request.method == 'POST':
		user_id = request.user.id
		search_text = request.POST['search_text']
		contacts = Contact.objects.filter(
			Q(user_id=user_id),
			Q(first_name__icontains=search_text) |
			Q(last_name__icontains=search_text) |
			Q(phone_number__icontains=search_text) |
			Q(email__icontains=search_text)
		)
		# render_to_reponse: save time for AJAX call due to not calling request
		return render_to_response(
			'core/searchcontact.html',
			{
				'contacts': contacts
			}
		)
	return render(
		request,
		'core/contact.html',
	)

@login_required(login_url='')
def logout_view(request):
	logout(request)
	return render(request, 'core/logout.html')
	
