from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)


class Device(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
