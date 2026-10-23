class Pet:
    def __init__(self, name, hunger=10, fun=10, health=10, energy=10):
        self.name = name
        self.hunger = hunger
        self.fun = fun
        self.health = health
        self.energy = energy
    def feed(self):
        self.hunger += 5
    def play(self):
        self.fun += 5
    def heal(self):
        self.health += 5
    def sleep(self):
        self.energy += 5

name = input("What would you like to name your pet?")
pet = Pet(name)
print(pet.name)