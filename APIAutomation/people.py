class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def person_description(self):
        description = "Name: " + self.name + ", Age " + str(self.age) + ", Height " + str(self.height)
        print(description)

    def get_weight(self):
        print("Person's weight is: " + str(self.weight))

    def update_weight(self, kg):
        self.weight = kg

# man.person_description()
# man.update_weight(107)
# man.get_weight()

girl = Person("Wendy", 8, 125)
# girl.person_description()
# girl.update_weight(36)
# girl.get_weight()
# print()


class Warrior(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.rage = 100  # ярость

    def get_rage(self):
        print(warrior.name + "'s rage is: " + str(self.rage))

    def person_description(self):
        description = "Name: " + self.name + ", Age " + str(self.age) + ", Rage " + str(self.rage)
        # print(description)
        return description


warrior = Warrior("Conan", 32, 200)
# warrior.person_description()
# warrior.update_weight(150)
# warrior.get_weight()
# warrior.get_rage()

# print("Description of player: " + warrior.person_description())
