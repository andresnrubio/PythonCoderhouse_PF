from django.shortcuts import HttpResponse,redirect
from django.template import loader
from blogApp.models import  comment, blogEntry

def redirectToHome(request):
    
    return redirect("/home/")
    
    
def home(request):

    template = loader.get_template("index.html")

    dictionary ={}
    
    document = template.render(dictionary)

    return HttpResponse(document)


def pages(request):

    template = loader.get_template("entryDetail.html")

    dictionary ={}
    
    document = template.render(dictionary)

    return HttpResponse(document)


def navBar(request):
    
    template = loader.get_template("navbar.html")

    dictionary ={}
    
    document = template.render(dictionary)

    return HttpResponse(document)