from django.shortcuts import HttpResponse
from django.template import loader
from blogApp.models import  comment, blogEntry


def home(request):

    template = loader.get_template("home.html")

    dictionary ={}
    
    document = template.render(dictionary)

    return HttpResponse(document)
