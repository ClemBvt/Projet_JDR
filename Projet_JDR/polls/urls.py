from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("attack/<int:sessionId>", views.attack, name="attack"),
    path("game/<int:session_id>/", views.game, name="game"),
    path("create/", views.createGame, name="createGame"),
]