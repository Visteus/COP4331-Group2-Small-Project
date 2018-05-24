from django.contrib import admin
from .models import users

# Access users with administrator privileges 
admin.site.register(users)