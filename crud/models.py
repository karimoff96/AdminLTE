from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Members(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=30)
    phone_number = models.IntegerField(blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username





