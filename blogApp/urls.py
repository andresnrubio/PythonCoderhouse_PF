from django.urls import path
from blogApp import views


urlpatterns = [
    path("", views.redirectToHome),
    path("home/", views.home, name="home"),
    # path("about/", views.about),
    path("pages/<entryId>", views.entryDetail, name="entryDetail"),
    path("home/elements.html", views.elements, name="elements"),
    path("pages/elements.html", views.elements, name="elements"),
    ]

