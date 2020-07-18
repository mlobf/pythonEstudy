from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.


def signupuser(request):
    """
        Aqui, primeiramente, separaremos os as requisicoes em GET, ao carregar
        _a pagina com as informaçoes do django, e POST, para trabalhar o envio das
        _dos dados para o Django.
        _O tratamento de erro de ocorre somente no POST, pois no GET, nao ha nada 
        _a ser tratado. Desta forma, usando o Try/Except,
        No try, a acao e, uma 
    """
    if request.method == "GET":
        return render(request, "todo/signupuser.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
            except IntegrityError:
                return render(request, "todo/signupuser.html", {"form": UserCreationForm(), 'error':'This user has already be taken'})
        else:
            return render(request, "todo/signupuser.html", {"form": UserCreationForm(), 'error':'Password did not match'})
        
        
