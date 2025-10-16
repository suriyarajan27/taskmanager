# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Todoo(models.Model):
    srno = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(User, max_length=25)

class Task(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True, auto_created=True)


class SignUpList(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  # remove null=True
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class LoginUpList(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
