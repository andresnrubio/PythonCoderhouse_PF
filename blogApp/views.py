from django.shortcuts import HttpResponse
from django.template import loader
from blogApp.models import user, comment, blogEntry


def home(request):
    users = user.objects.all()

    template = loader.get_template("home.html")

    dictionary = {"users": users}
    print(dictionary)
    document = template.render(dictionary)

    return HttpResponse(document)
