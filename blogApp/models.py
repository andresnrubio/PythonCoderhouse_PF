from django.db import models


class blogEntry(models.Model):
    title = models.CharField(max_length=120)
    imgUrl = models.CharField(max_length=100)
    date = models.DateField()
    content = models.CharField(max_length=5000)


class comment(models.Model):
    username = models.CharField(max_length=50)
    comment = models.CharField(max_length=400)
    date = models.DateField()


class user(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
