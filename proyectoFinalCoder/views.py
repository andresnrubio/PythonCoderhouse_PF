from django.shortcuts import HttpResponse
from django.template import loader

# from proyectoFinalCoder.models import user


def login(request):
    # users = user.objects.all()

    template = loader.get_template("login.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)


def register(request):
    
    
    template = loader.get_template("register.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)
