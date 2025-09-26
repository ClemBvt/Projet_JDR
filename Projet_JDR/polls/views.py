from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import GameSession, Character
from django.utils import timezone
import random

# Create your views here.
def index(request):
    player1 = Character("Pierre")
    ennemi1 = Character("Mechant")
    
    return render(request, "polls/index.html", {"player1": player1, "ennemi": ennemi1})

def attack(request, sessionId):
    session = get_object_or_404(GameSession, pk=sessionId)
    session.status == "finish"
    session.save()
    if session.turn == 0:
        session.enemy.hp -= session.character.attack
        session.enemy.save()
        if session.enemy.hp <= 0:
            session.status = "finish"
            session.save()
            return redirect('game', session_id=session.id)
        session.turn = 1
        session.save()
    else:
        session.character.hp -= session.enemy.attack
        session.character.save()
        if session.character.hp <= 0:
            session.status = "finish"
            session.save()
            return redirect('game', session_id=session.id)
        session.turn = 0
    session.save()
    return redirect('game', session_id=session.id)

def createGame(request):
    namePlayer = request.POST.get("character_name")
    character = Character.objects.create(name=namePlayer)
    enemy = Character.objects.create(
        name="Ennemi",
        attack=20,
        hp=80
    )
    session = GameSession.objects.create(
        status="Current",
        character=character,
        enemy=enemy,
    )
    session.save()
    return redirect('game', session_id=session.id)


def game(request, session_id):
    session = get_object_or_404(GameSession, pk=session_id)
    return render(request, "polls/game.html", {"session": session})
