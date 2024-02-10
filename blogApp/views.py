from django.shortcuts import HttpResponse, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import os
from blogApp.models import Comment, BlogEntry, user
from blogApp.forms import newEntryForm, signupForm, loginForm
from datetime import datetime


def redirectToHome(request):
    return redirect("/home/")


def home(request):
    entries = BlogEntry.objects.all()

    template = loader.get_template("index.html")

    admin = True

    dictionary = {"entries": entries, "admin": admin}

    document = template.render(dictionary)

    return HttpResponse(document)


def entryDetail(request, entryId):
    entry = BlogEntry.objects.get(pk=entryId)

    print(entry)
    admin = True

    template = loader.get_template("entryDetail.html")

    dictionary = {"entry": entry, "admin": admin}

    document = template.render(dictionary)

    return HttpResponse(document)


def handle_uploaded_file(f):
    directory = "blogApp/static/assets"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, f.name), "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def newEntry(request):
    if request.method == "POST":
        form = newEntryForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data

            title = informacion["title"]
            subtitle = informacion["subtitle"]
            introduction = informacion["introduction"]
            resume = informacion["resume"]
            content_list = []
            content_list.append(informacion["content_list_1"])
            content_list.append(informacion["content_list_2"])
            content_list.append(informacion["content_list_3"])
            content_list.append(informacion["content_list_4"])
            content_list.append(informacion["content_list_5"])
            filtered_list = [item for item in content_list if item != ""]
            author = informacion["author"]
            image_file = request.FILES["imgUrl"]
            imgUrl = image_file.name
            handle_uploaded_file(image_file)
            image_file_logo = request.FILES["imgLogo"]
            imgLogo = image_file_logo.name
            handle_uploaded_file(image_file_logo)

            current_date = datetime.now().date()
            formatted_date = current_date.strftime("%Y-%m-%d")

            newEntry = BlogEntry(
                title=title,
                subtitle=subtitle,
                introduction=introduction,
                resume=resume,
                content_list=filtered_list,
                author=author,
                imgUrl=imgUrl,
                imgLogo=imgLogo,
                date=formatted_date,
            )

            newEntry.save()

            template = loader.get_template("entryDetail.html")

            dictionary = {
                "entry": {
                    "title": title,
                    "subtitle": subtitle,
                    "introduction": introduction,
                    "resume": resume,
                    "content_list": filtered_list,
                    "author": author,
                    "imgUrl": imgUrl,
                    "imgLogo": imgLogo,
                }
            }
            document = template.render(dictionary)

            return HttpResponse(document)
    # else:
    admin = True

    places = []

    template = loader.get_template("newEntry.html")

    dictionary = {"admin": admin, "places": places}

    document = template.render(dictionary)

    # return render(request, "newentry/" , dictiona ry)

    return HttpResponse(document)


def about(request):
    template = loader.get_template("about.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)


def elements(request):
    template = loader.get_template("elements.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)


@csrf_exempt
def login(request):
    # users = user.objects.all()

    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data

            print(informacion)

    template = loader.get_template("login.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)


@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            
            newUser = user(
                name=informacion["name"],
                lastname=informacion["lastname"],
                email=informacion["email"],
                password=informacion["password"],
            )
            
            newUser.save()
            
            return redirect("/")
            
            # template = loader.get_template("index.html")

            # dictionary = {"admin": True}

            # document = template.render(dictionary)

            # return HttpResponse(document)
            

    template = loader.get_template("signup.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)
