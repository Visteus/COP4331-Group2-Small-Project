from django.db import models

# Create users table
class users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
 
# Create contacts table. "user_fk" is a foreign key to users
# on_delete=CASCADE ==> if user gets deleted, drop all contacts    
class contacts(models.Model):
    user_fk = models.ForeignKey(users, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()