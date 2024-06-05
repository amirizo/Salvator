from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .models import *
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
    questions = QuestionCategory.objects.all()

    context = {
        'questions': questions
    }
    return render(request, "salvatore/Question.html", context )


def question_detail(request, pk):
    category = QuestionCategory.objects.get(id=pk)

    questions = Question.objects.filter(category=category)
    context = {
        'questions': questions,
        'category':category
        # 'exercise':exercise
        
    }

    return render(request, 'salvatore/question_detail.html',context )



def submit_answers(request, pk, quest_id):
    if request.method == 'POST':
        category = QuestionCategory.objects.get(id=pk)
        questions = Question.objects.filter(category=category, id__gt=quest_id).exclude(id=quest_id)
        if 'next' in request.POST:
            if questions:
                quest = Question.objects.get(id=quest_id)
                user = request.user
                answer = 'Not Submited'
                UserSubmittedAnswer.objects.create(user=user,question=quest,right_answer=answer)
                context = {
                    'questions': questions,
                    'category':category
                    # 'exercise':exercise
                    
                }
                return render(request, 'salvatore/question_detail.html',context )
        else:
            quest = Question.objects.get(id=quest_id)
            user = request.user
            answer = request.POST['question']
            UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
        if questions:
            context = {
                'questions': questions,
                'category':category
                # 'exercise':exercise
                
            }
            return render(request, 'salvatore/question_detail.html',context )
        else:
            result = UserSubmittedAnswer.objects.filter(user=request.user)
            context = {
                'result': result,  
            }
            return render(request, 'salvatore/result.html',context )
    
    else:
        return HttpResponse("methodnot allowed")


