from django.urls import path
from django.contrib.auth.views import logout
from . import views

app_name = 'core'

urlpatterns = [
    # Core
    path('contacts/', views.contact_view, name='contact_view'),

    # login, logout, new contact, new user
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('contacts/newcontact/', views.create_contact, name='create_contact'),
    path('newuser/', views.create_user, name='create_user'),
    path('', views.login_view, name='login_view'),

]
