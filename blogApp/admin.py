from django.contrib import admin
from .models import BlogEntry, Comment, user
# Register your models here.

admin.site.register(BlogEntry)
admin.site.register(Comment)
admin.site.register(user)