from django.shortcuts import HttpResponse,redirect
from django.template import loader
from blogApp.models import  Comment, BlogEntry

def redirectToHome(request):
    
    return redirect("/home/")
    
    
def home(request):

    entries = BlogEntry.objects.all()

    template = loader.get_template("index.html")

    dictionary ={ 'entries': entries }
        
    document = template.render(dictionary)

    return HttpResponse(document)


def pages(request):

    template = loader.get_template("entryDetail.html")

    dictionary ={}
    
    document = template.render(dictionary)

    return HttpResponse(document)


def entryDetail(request, entryId):

    entry = BlogEntry.objects.get(pk=entryId)


    template = loader.get_template("entryDetail.html")

    dictionary ={ 'entry': entry }
    
    document = template.render(dictionary)

    return HttpResponse(document)

def elements(request):

    template = loader.get_template("elements.html")

    dictionary ={}
    
    document = template.render(dictionary)

    return HttpResponse(document)

def navBar(request):
    
    template = loader.get_template("navbar.html")

    dictionary ={}
    
    document = template.render(dictionary)

    return HttpResponse(document)