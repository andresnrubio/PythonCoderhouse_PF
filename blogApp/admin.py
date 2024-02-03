from django.contrib import admin
from .models import BlogEntry, Comment
# Register your models here.

admin.site.register(BlogEntry)
admin.site.register(Comment)