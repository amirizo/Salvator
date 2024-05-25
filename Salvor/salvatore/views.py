from django.shortcuts import render,HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
# Create your views here.
def SignUp(request):
    context = {}
    if request.method == 'GET':
        return render(request, "salvatore/registration.html", context)

    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        existing_user = User.objects.filter(username=username).first()

        if not existing_user:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password
            )

            login(request, user)
            return redirect("index")

        
        return render(request, "salvatore/registration.html", context)


def SignIn(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        context['message'] = "Invalid username or password."
        return render(
            request,
            "salvatore/login.html",
            context
        )
    return render(request, "salvatore/login.html", context)



def logout_request(request):
    logout(request)
    return redirect('index')


def index(request):
    return render(request, "salvatore/index.html")


def classes(request):
    return render(request, "salvatore/classes.html")


def question(request):
    return render(request, "salvatore/Question.html")