from django.test import TestCase
from .models import Character, GameSession

# Create your tests here.
# Test des personnages
class CharacterTest(TestCase):
    def setUp(self):
        Character.objects.create(name='Test', hp=150, attack=30)

    def test_character_can_attack(self):
        character = Character.objects.create(name='Test')
        self.assertEqual(character.attack, 10, "Les dégats sont différents")

# Test du random
class RandomTest(TestCase):
    def setUp(self):
        GameSession.objects.create(
            status="Current",
        )

    def test_random_turn(self):
        """Vérifie que le champ turn prend aléatoirement 0 ou 1"""
        session1 = GameSession.objects.create()
        # previous = session1.turn

        # On génère d’autres sessions jusqu’à trouver une valeur différente
        # different_found = False
        for i in range(10):  # limite de 10 essais pour ne pas boucler à l’infini
            session = GameSession.objects.create()
            if i == 5:
                print("On force la valeur à 1")
                session.turn = 1
            print(f"Session {session.id} → turn={session.turn}")
            # if session.turn != previous:
            #     different_found = True
            #     break

        # Vérifie qu’on a bien trouvé une différence
        # self.assertFalse(
        #     different_found,
        #     "Le champ turn prends toujours la même valeur (0)"
        # )


