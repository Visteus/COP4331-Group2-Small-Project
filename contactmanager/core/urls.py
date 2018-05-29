from django.urls import path
from django.contrib.auth.views import logout
from . import views

app_name = 'core'

urlpatterns = [
    path('contacts/', views.contact_view, name='contact_view'),
    path('contacts/newcontact/', views.create_new_contact, name='create_new_contact'),
    path('contacts/contactdetail/<int:contact_id>/', views.contact_detail_view, name='contact_detail_view'),
    path('contacts/editcontact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('logout/', views.logout_view, name='logout_view'),

    # require login 
    path('newuser/', views.create_new_user, name='create_new_user'),
    path('', views.login_view, name='login_view'),
]   
