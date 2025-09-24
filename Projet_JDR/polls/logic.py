class Character:
    # Constructeur
    def __init__(self, name, hp=100, attack=10, objects=None):
        self._name = name
        self._hp = hp
        self._attack = attack
        self._object = objects

    # Getters
    def getName(self):
        return self._name

    def getHp(self):
        return self._hp
    
    def getAttack(self):
        return self._attack
    
    def getObject(self):
        return self._object

    # Setters
    def setName(self, name):
        self._name = name
    
    def setHp(self, hp):
        self._hp = hp
        return print("ok")

    def setAttack(self, attack):
        self._attack = attack
    
    def setObject(self, object):
        self._object = object

    # Attaquer
    def attack(self, cible):
        cible.hp -=  self.attack

    
class Objects:
    # Constructeur
    def __init__(self, name, type):
        self._name = name
        self._type = type

    # Getter
    def getName(self):
        return self._name

    def getType(self):
        return self._type

    # Setter
    def setName(self, name):
        self._name = name

    def setType(self, type):
        self._type = type
    
class Sword(Objects):
    # Constructeur
    def __init__(self, attack=10):
        self._attack = attack

    # Getter
    def getAttack(self):
        return self._attack
    
    # Setter
    def setAttack(self, attack):
        self._attack = attack

    # Augmenter le niveau d'attaque
    def increaseAttack(self, cible):
        cible.attack += self._attack

class Potion(Objects):
    # Constructeur
    def __init__(self, hp=10):
        self._hp = hp

    # Getter
    def getHp(self):
        return self._hp

    # Setter
    def setHp(self, hp):
        self._hp = hp
        
    # Augmenter le niveau de vie
    def increaseLife(self, cible):
        cible.hp = self._hp 
