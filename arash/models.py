from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
