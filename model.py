# Characters 
class Characters:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attacking(self, other):
        other.defending(self.attack)

    def defending(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def alive(self):
        return self.health > 0

# Hero
class Hero(Characters):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

# Warrior
class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, health=150, attack=25)

    def attacking(self, other):
        print(f"{self.name} strikes with the light saber!")
        super().attacking(other)

# Warlock
class Warlock(Hero):
    def __init__(self, name):
        super().__init__(name, health=200, attack=40)

    def attacking(self, other):
        print(f"{self.name} cast a spell, infernum!")
        super().attacking(other)

# Monster
class Monster(Characters):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

# Ogre - Weak against Warriors, Strong agains Warlocks
class Ogre(Monster):
    def __init__(self):
        super().__init__(name="Cavern Troll", health=140, attack=10)

# Dragon - Weak against Warlock, Strong against Warriors
class Dragon(Monster):
    def __init__(self):
        super().__init__(name="Ryu", health=180, attack=30)