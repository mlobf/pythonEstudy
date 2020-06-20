from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password':'hasdfasfiahfaish'})

def eggs(request):
    return HttpResponse("<h1>Who here like eggs more than me?!!</h1>")
