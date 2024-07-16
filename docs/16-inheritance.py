class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print("Breathing")


# Class can be inherited by passing the class to inherit from in between parentheses
class Fish(Animal):
    def __init__(self, name):
        # you need to call the init in the super class
        super().__init__(name)

    # no need to define breath since it's part of the super class

    def announce(self):
        # You can also access properties defined in the super class
        print(f"I'm a {self.name}")

    # You can also extend the behavior by calling the super method
    def breathe(self):
        super().breathe()
        print("Underwater")

    def swim(self):
        print("Swiming")


gold_fish = Fish("Gold Fish")
clown_fish = Fish("Clown Fish")
shark = Fish("Shark")

shark.breathe()
shark.swim()

clown_fish.announce()
