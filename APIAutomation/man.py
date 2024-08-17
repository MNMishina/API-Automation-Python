from people import Person, Warrior

man = Person("David", 47, 182)
man.person_description()

warrior = Warrior("Conan", 32, 200)
print("Description of player: " + warrior.person_description())