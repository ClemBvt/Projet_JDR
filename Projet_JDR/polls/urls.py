from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/setName", views.setName, name="setName"),
    path("/attack", views.attack, name="attack"),
]
