from django.db import models

# Create your models here.
# models.py
from django.db import models

# Classe de base pour les objets
class GameObject(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True  # On n'a pas besoin de créer une table pour cette classe de base

    def __str__(self):
        return self.name

# Épée
class Sword(GameObject):
    attack = models.IntegerField(default=10)

    def increase_attack(self, target):
        target.attack += self.attack
        target.save()

# Potion
class Potion(GameObject):
    hp = models.IntegerField(default=10)

    def increase_life(self, target):
        target.hp += self.hp
        target.save()

# Personnage
class Character(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=10)
    # On peut lier un objet (Sword ou Potion) via une clé étrangère optionnelle
    sword = models.ForeignKey(Sword, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    potion = models.ForeignKey(Potion, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    # Attaquer une cible
    def attack_target(self, target):
        target.hp -= self.attack
        target.save()

class GameSession(models.Model):
    turn = models.IntegerField(default=0)
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True, related_name="as_main_character_sessions",)
    enemy = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True, related_name="as_enemy_sessions",)
    status = models.CharField(max_length=100)
    current_player = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True, related_name="as_current_player_sessions",)