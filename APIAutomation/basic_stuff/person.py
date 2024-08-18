class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person is created")

    def sing(self):
        print(self.name + " is singing")

    def dance(self):
        print(self.name + " is dancing")


woman = Person("Jules", 30)
print("Woman's name is " + woman.name)
woman.dance()
woman.sing()

man = Person("Alan", 17)
print("Man's name is " + man.name)
man.sing()
man.dance()
