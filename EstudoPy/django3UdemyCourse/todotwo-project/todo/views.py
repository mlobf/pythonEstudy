from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate 
from .forms import TodoForm

# Create your views here.


def home(request):
    return render(request, "todo/home.html")


def signupuser(request):
    """
    Aqui, primeiramente, separaremos os as requisições em GET, ao carregar
        _a pagina com as informações do django, e POST, para trabalhar o envio das
        _dos dados para o Django.
        _O tratamento de erro de ocorre somente no POST, pois no GET, nao ha nada
        _a ser tratado. Desta forma, usando o Try/Except,
        No try, uma vez com as senhas conferidas, o usuario e criado /salvo.
    """
    if request.method == "GET":
        return render(request, "todo/signupuser.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("currenttodos")
            except IntegrityError:
                return render(
                    request,
                    "todo/signupuser.html",
                    {
                        "form": UserCreationForm(),
                        "error": "This user has already be taken",
                    },
                )
        else:
            return render(
                request,
                "todo/signupuser.html",
                {"form": UserCreationForm(), "error": "Password did not match"},
            )


def currenttodos(request):
    return render(request, "todo/currenttodos.html")


def loginuser(request):
    if request.method == "GET":
        return render(request, "todo/loginuser.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "todo/loginuser.html",
                {
                    "form": AuthenticationForm(),
                    "error": "Username and password did not match",
                },
            )
        else:
            login(request, user)
            return redirect("currenttodos")


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")

def createtodo(request):
    if request.method == "GET":
        return render(request, 'todo/createtodo.html',{'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'error':'Bad Data pass in'})


