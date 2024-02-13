from django.contrib import admin
from .models import BlogEntry, user
# Register your models here.

admin.site.register(BlogEntry)
admin.site.register(user)