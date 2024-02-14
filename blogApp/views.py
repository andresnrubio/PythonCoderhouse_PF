from django.shortcuts import HttpResponse, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import os
from blogApp.models import BlogEntry, user
from blogApp.forms import newEntryForm, signupForm, loginForm, commentForm
from datetime import datetime
from django.utils import timezone
from django.contrib import messages


def redirectToHome(request):
    return redirect("/home/")


def home(request):
    entries = BlogEntry.objects.all()

    template = loader.get_template("index.html")

    user = {}

    if "logged" in request.session:
        user["role"] = request.session["role"]
        print(user)

    dictionary = {"entries": entries, "user": user}

    document = template.render(dictionary)

    return HttpResponse(document)


@csrf_exempt
def entryDetail(request, entryId):
    entry = BlogEntry.objects.get(pk=entryId)

    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():

            current_date = timezone.now()
                
            newComment = {
                "comment": request.POST["comment"],
                "fullname": f"{request.session['name']} {request.session['lastname']}",
                "date": current_date.strftime("%Y-%m-%d")
            }
            entry.comment_list.append(newComment)
            
            entry.save()
        else:
            if "action" in request.POST:
                action = request.POST.get("action")
                if action == "delete":
                    entry.comment_list.pop(int(request.POST['id']) - 1)
                    entry.save()
                    pass
                elif action == "submit":
                    updated_comment = request.POST.get(f"textarea{request.POST['id']}")
                    entry.comment_list[int(request.POST['id']) - 1]["comment"] = updated_comment
                    entry.save()
                    pass

    user = {}

    if "logged" in request.session:
        user["role"] = request.session["role"]
        user["fullname"] = f"{request.session['name']} {request.session['lastname']}"


    template = loader.get_template("entryDetail.html")

    dictionary = {"entry": entry, "user": user}

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
    admin = True

    places = []

    template = loader.get_template("newEntry.html")

    dictionary = {"admin": admin, "places": places}

    document = template.render(dictionary)

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
            email = request.POST.get("email")
            password = request.POST.get("password")
            try:
                userExists = user.objects.get(email=email)
                if userExists.password == password:
                    request.session["name"] = userExists.name
                    request.session["lastname"] = userExists.lastname
                    request.session["email"] = userExists.email
                    request.session["role"] = userExists.role
                    request.session["logged"] = True

                    return redirect("/home/")
                else:
                    messages.error(request, "Invalid email or password.")
            except user.DoesNotExist:
                messages.error(request, "Invalid email or password.")

    template = loader.get_template("login.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)


def logout(request):
    request.session.flush()

    return redirect("/login/")


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

    template = loader.get_template("signup.html")

    dictionary = {}

    document = template.render(dictionary)

    return HttpResponse(document)
