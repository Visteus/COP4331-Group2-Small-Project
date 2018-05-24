from django.urls import path
from . import views

urlpatterns = [
    # Core
    path('', views.index, name='index'),
    
    # login
    path('login', views.login, name='login'),
]