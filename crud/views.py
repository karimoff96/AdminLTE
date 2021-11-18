from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.
def login1(request):
    return render(request, "register.html")


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect('/index')
    else:
        return render(request, 'login.html')


def index(request):
    task = len(Task.objects.all())
    return render(request, "index.html", {'task':task})


def register(request):
    if request.method == "POST":
        a = request.POST
        user = Members.objects.create(
            first_name=a['first_name'],
            last_name=a['last_name'],
            email=a["email"],
            phone_number=a['phone_number'],
            birth_date=a['birth_date'],
            username=a["username"],
            password=a["password"],
        )
        user.save()
        return redirect('/index')
    return render(request, 'register.html')


def home(request):
    task = Task.objects.all()
    if request.method == "POST":
        a = request.POST
        task = Task.objects.create(
            name=a['task_name']
        )
        task.save()
        return redirect('/home/')
    return render(request, "todolist.html", {"task": task})


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/home')


def edit(request, id):
    print(request.POST)
    task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    if request.method == 'POST':
        a = request.POST
        task.name = a["task_name"]
        task.save()
        return redirect('/home')
    return render(request, "todolist_edit.html", {'task': task, 'tasks': tasks})


def forgot_password(request):
    return render(request, 'forgot-password.html')


def gallery(request):
    return render(request, 'gallery.html')


def members(request):
    member = Members.objects.all()
    if request.method == "POST":
        a = request.POST
        member = Members.objects.create(
            first_name=a['first_name'],
            last_name=a['last_name'],
            email=a['email'],
            phone_number=a['phone_number'],
            birth_date=a['birth_date'],
            username=a['username'],
        )
        member.save()
        return redirect('/members/')
    return render(request, 'members.html', {'members': member})
