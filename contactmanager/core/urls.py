from django.urls import path
from django.contrib.auth.views import logout
from . import views

app_name = 'core'

urlpatterns = [
    # Core
    path('contacts/', views.index, name='index'),
    # login, logout
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

]   