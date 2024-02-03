from django.db import models

class BlogEntry(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)
    introduction = models.CharField(max_length=5000)
    content_list = models.JSONField(default=list, null=True) 
    resume = models.CharField(max_length=5000, null=True)
    author = models.CharField(max_length=120, default="Anonimo")
    imgUrl = models.CharField(max_length=100, null=True)
    imgLogo= models.CharField(max_length=100, null=True)
    date = models.DateField()
    
class Comment(models.Model):
    username = models.CharField(max_length=50)
    comment = models.CharField(max_length=400)
    date = models.DateField()


# class user(models.Model):
#     username = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
