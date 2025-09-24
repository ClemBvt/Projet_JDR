from django.shortcuts import render
from django.http import HttpResponse
from .logic import Character
from django.shortcuts import redirect


# Create your views here.

def index(request):
    player1 = Character("Pierre")
    ennemi1 = Character("Mechant")
    
    return render(request, "polls/index.html", {"player1": player1, "ennemi": ennemi1})

def setName(request):
    player = Character("")
    player.setName(request.POST.get("character_name"))

    return render(request, "polls/index.html", {"player": player})

def attack(request):
     return redirect('index')