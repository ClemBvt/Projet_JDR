Rapport :

On commence par entrer son nom d’utilisateur et le jeu se lance.
La personne qui commence au premier tour est définie aléatoirement (l’utilisateur ou l’ennemi). Cette fonction a été modifiée pour les tests, le premier tour est donc défini manuellement.
Lorsque le tour est à l’utilisateur, il clique sur « Attaquer » pour infliger des dégâts à l’ennemi. Les points HP de l’ennemi diminuent. Le tour passe alors à l’ennemi.
Lorsque le tour est à l’ennemi, l’utilisateur doit cliquer sur « Continuer » pour pouvoir voir les résultats de l’attaque qu’il aura reçue. Les points HP de l’utilisateur diminuent. Le tour passe alors à l’utilisateur.

Codé en Python Django JS

Comment lancer l'application :
- Avoir installé Django
- Lancer le serveur (python3 manage.py runserver)
- Aller sur l'URL localhost:8000

Comment exécuter les tests :
- Lancer les tests Django à partir du répertoire /Projet_JDR/Projet_JDR/polls/tests.py
- Lancer les tests Selenium à partir du répertoire /Projet_JDR/test.py

Tests unitaires :
- test_character_can_attack : Teste si la fonction attaquer du personnage de l’utilisateur fonctionne.

Test sur une fonction aléatoire : 
- test_random_turn : Vérifie que le premier tour est bien donné à l'utilisateur ou  au perosnnage aléatoirement. Par défault le test commence de 0, puis on force à passer à 1.

Test en selenium :
- testCharacter : Test les fonctions de créer un personnage et attaquer l'ennemi.

