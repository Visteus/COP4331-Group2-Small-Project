from django.contrib import admin
from core.models import Contact
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Contact)