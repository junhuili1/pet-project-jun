import random

class Pet:
    def __init__(self, name, hunger=random.randint(5,10), fun=random.randint(5,10), health=random.randint(5,10), energy=random.randint(5,10)):
        self.name = name
        self.hunger = hunger
        self.fun = fun
        self.health = health
        self.energy = energy
    def feed(self):
        self.hunger += random.randint(3,7)
    def play(self):
        self.fun += random.randint(3,7)
    def heal(self):
        self.health += random.randint(3,7)
    def sleep(self):
        self.energy += random.randint(3,7)

name = input("What would you like to name your pet?").capitalize()
pet = Pet(name)
while True:
    if pet.hunger < 1:
        pet.health -= 1
        pet.energy -= 2
    if pet.fun < 1:
        pet.energy -= 1
    if pet.energy < 1:
        pet.health -= 1
    if pet.health < 1:
        print("Your pet has died. Game over.")
        break

    print(pet.name)
    print("-----------------------------------------------------------")
    print(f"Hunger: {pet.hunger} | Fun: {pet.fun} | Health: {pet.health} | Energy: {pet.energy}")
    print(f"[1] Feed {pet.name}")
    print(f"[2] Play with {pet.name}")
    print("[3] Go to the vet")
    print(f"[4] Put {pet.name} to sleep")
    print(f"[q] Quit program")
    action = input("What would you like to choose? Input the number of what you would like to do.")
    print(" ")
    print(" ")
    print(" ")

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
        print("can you not read...?")

    pet.hunger -= random.randint(0,2)
    pet.fun -= random.randint(0,2)
    pet.health -= random.randint(0,2)
    pet.energy -= random.randint(0,2)