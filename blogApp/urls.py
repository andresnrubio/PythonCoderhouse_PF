from django.urls import path
from blogApp import views


urlpatterns = [
    path("", views.redirectToHome),
    path("home/", views.home, name="home"),
    path("about/", views.about),
    path("pages/<entryId>", views.entryDetail, name="entryDetail"),
    path("elements/", views.elements, name="elements"),
    path("newentry/", views.newEntry, name="newentry"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    ]

