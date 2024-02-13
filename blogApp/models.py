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
    comment_list = models.JSONField(default=list, null=True) 

    def __str__(self) -> str:
        return super().__str__()
    
# class Comment(models.Model):
#     fullname = models.CharField(max_length=100, default="Anonimo")
#     comment = models.CharField(max_length=400)
#     date = models.DateField()

class user(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('visitor', 'Visitor'),
        ('moderator', 'Moderator'),
    ]

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="visitor")
    
    def __str__(self) -> str:
        return super().__str__()


