from model import Warrior, Warlock, Ogre, Dragon

print ("Time for Battle!\n")
# Battle
def battle(hero, monster):
    print(f"{hero.name} VS {monster.name}!")
    while hero.alive() and monster.alive():
        hero.attacking(monster)
        if monster.alive():
            monster.attacking(hero)
        
        print(f"{hero.name} health: {hero.health}, {monster.name} health: {monster.health}")
        
    if hero.alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{monster.name} wins!")

# Execute
if __name__ == "__main__":
    # Champions
    warrior = Warrior("Luke Skywalker")
    warlock = Warlock("Merlin")

    # Monsters
    ogre = Ogre()
    dragon = Dragon()

    # Battles
    battle(warrior, ogre)
    battle(warlock, dragon)
    
print ("Stay Tuned For The Next Battle!!")