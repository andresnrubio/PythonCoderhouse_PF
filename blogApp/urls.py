from django.urls import path
from blogApp import views


urlpatterns = [path("", views.home, name="home")]
