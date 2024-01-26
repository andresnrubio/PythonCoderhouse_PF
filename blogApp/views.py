from django.shortcuts import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    template = loader.get_template("home.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)
