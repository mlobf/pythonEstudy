from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'message':'this is my first message.'
    }

    return render(request,'posts/index.html', context)
