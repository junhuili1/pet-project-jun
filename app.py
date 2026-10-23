import random

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

name = input("What would you like to name your pet?").capitalize()
pet = Pet(name)
while True:
    print(pet.name)
    print("-----------------------------------------------------------")
    print(f"Hunger: {pet.hunger} | Fun: {pet.fun} | Health: {pet.health} | Energy: {pet.energy}")
    print(f"[1] Feed {pet.name}")
    print(f"[2] Play with {pet.name}")
    print("[3] Go to the vet")
    print(f"[4] Put {pet.name} to sleep")
    action = input("What would you like to choose? Input the number of what you would like to do.")
    if action == "1":
        pet.feed()
    elif action == "2":
        pet.play()
    elif action == "3":
        pet.heal()
    elif action == "4":
        pet.sleep()
    elif action == "q":
        break    
    else:
        print("can you not read numbers...?")