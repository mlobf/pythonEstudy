from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "generator/home.html")


def password(request):

    thepassword = "testing"

    return render(request, "generator/password.html", {"password": thepassword})
