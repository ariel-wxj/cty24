import random


class character:
    def __init__(self, name, health,strength,rizz):
        self.health = health
        self.strength = strength
        self.rizz = rizz
        self.name = name
    def whatCharacter(self):
        print("my name is{self.name}")
    def takeDmg(self, takeDamage):
        self.health = self.health - takeDamage
        if self.health <= 0:
            print("you died")
    # def dealDmg(self, damage):
    #     self.health = self.health - damage
    def rizz(self, rizz):
        self.health = self.health + rizz

Rizzio=character("Rizzio",100,20,10)
Rizzman=character("Rizzman",100,60,15)
Spiderrizz=character("Spiderrizz",100,30,10)
Rizzachu=character("Rizzachu",100,50,15)
Batsigma=character("Batsigma",100,20,0)


"""abilities={
    "Rizzio":"bad side : Jump"
    "rizzman" "bad side: pew pew",
    "rizzachu":"our side: generates electricity",
    "spiderrizz":"bad side: makes spider webs",
    "batsigma":"our side: protects people"
}
"""
print("welcome to the skibbler game! you will fight monsters and maintain your health and strength")
print("here are the rules and instructions")

print("you will try to kill every character who isnt on the same side as you to win.")
input("press enter to continue")
print("the characters on your team are Rizzachu and Batsigma")
input("press enter to continue")
print("strength is how much damage you can deal")
input("press enter to continue")
print("rizz is how much you can heal")
input("press enter to continue")
print("health is how much hp you have")
input("press enter to continue")
print("when you attack a character there is a chance the attack will backfire on you")
input("press enter to continue")
print("goodluck!")
input("press enter to continue")

player1 = str(input("what do you want to be named:"))
player1 = character(player1,100,80,15)
rizz = 15
health = 100
strength = 80
done = bool(False)

print("here are the character stats")
input("press enter to continue")
# print(character("Rizzio",100,20,10))
print(f'My name is {Rizzio.name}, I have {Rizzio.health} HP Points, I have {Rizzio.strength} strength, and I have {Rizzio.rizz} rizz')
input("press enter to continue")
# print(character("Rizzman",100,60,15))
print(f'My name is {Rizzman.name}, I have {Rizzman.health} HP Points, I have {Rizzman.strength} strength, and I have {Rizzman.rizz} rizz')
input("press enter to continue")
# print(character("Spiderrizz",100,30,10))
print(f'My name is {Spiderrizz.name}, I have {Spiderrizz.health} HP Points, I have {Spiderrizz.strength} strength, and I have {Spiderrizz.rizz} rizz')
input("press enter to continue")
# print(character("Batsigma",100,20,0))
print(f'My name is {Batsigma.name}, I have {Batsigma.health} HP Points, I have {Batsigma.strength} strength, and I have {Batsigma.rizz} rizz')
input("press enter to continue")
# print(character("Rizzachu",100,50,15))
print(f'My name is {Rizzachu.name}, I have {Rizzachu.health} HP Points, I have {Rizzachu.strength} strength, and I have {Rizzachu.rizz} rizz')
input("press enter to continue")

print("you have", rizz, "rizz")
print("you have", health, "health")
print("you have", strength, "strength")
print("you have the ability to fly")



A = "A. Upgrade your rizz"
B = "B. Fight Rizzio. He has the ability to jump very high"
C = "C. Fight Rizzman. He has the ability to shoot poeple"
D = "D. Fight spiderrizz. He has the ability to make spider webs"
E = "E. Status check"
F = "F. Get rizzachu to help you. he can generate electricity"
G = "G. get batsigma to help you. He can protect people"
H = "H. Check another characters status"
I = "I. Use Rizz"
Q = "Q. quit"


chance = random.randint(1,10)

while done == False:
    print(A)
    print(B)
    print(C)
    print(D)
    print(E)
    print(F)
    print(G)
    print(H)
    print(I)
    print(Q)
    playerInput=input("choose one:")
    if playerInput == "A":
        if chance >= 5:
            rizz += chance
        else:
            rizz = rizz
    elif playerInput == "B":
        if chance >= 3:
            Rizzio.health -= player1.strength
            print("you succeeded")
            print(f"Rizzio now has {Rizzio.health} health left")
        else: 
            player1.health -= Rizzio.strength
            print("you failed")
            print(f"you now have {player1.health} health left")
    elif playerInput == "C":
        if chance >= 3:
            Rizzman.health -= player1.strength
            print("you succeeded")
            print(f"Rizzman now has {Rizzman.health} health left")
        else: 
            player1.health -= Rizzman.strength
            print("you failed")
            print(f"you now have {player1.health} health left")
    elif playerInput == "D":
        if chance >= 3:
            Spiderrizz.health -= player1.strength
            print("you succeeded")
            print(f"Spiderrizz now has {Spiderrizz.health} health left")
        else: 
            player1.health -= Spiderrizz.strength
            print("you failed")
            print(f"Spiderrizz now has {Spiderrizz.health} health left")
    elif playerInput == "E":
        print("you have", rizz, "rizz")
        print("you have", health, "health")
        print("you have", strength, "strength")
        print("you have the ability to fly")
    elif playerInput == "F":
        print("1. Attack")
        print("2. Heal")
        choice = int(input("what do you want Rizzachu to help you with?:"))
        if choice == 1:
            print("which character do you want to attack")
            print("1. Rizzio")
            print("2. Rizzman")
            print("3. Spiderrizz")
            Attack = str(input("Who do you want to attack?:"))
            if Attack == "Rizzio":
                if chance >= 3:
                    Rizzio.health -= Rizzachu.strength
                    print("Attack sucessful")
                else:
                    Rizzachu.health -= Rizzio.strength
                    print("Attack failed")
            elif Attack == "Rizzman":
                if chance >= 3:
                    Rizzman.health -= Rizzachu.strength
                    print("attack sucessful")
                else:
                    Rizzachu.health -= Rizzman.strength
                    print("attack failed")
            elif Attack == "Spiderrizz":
                if chance >= 3:
                    Spiderrizz.health -= Rizzachu.strength
                    print("attack sucessful")
                else:
                    Spiderrizz.health -= Rizzman.strength
                    print("attack failed")
            else:
                print("error")
        if choice == 2:
            print("which character do you want to heal")
            print("1. Batsigma")
            print("2.", player1)
            Heal = str(input("Who do you want to Heal?:"))
            if Heal == "Batsigma":
                Batsigma.health += Rizzachu.rizz
                print(f"Batsigma now has {Batsigma.health} health")
            elif Heal == player1:
                player1.health += Rizzachu.rizz
                print(f"{player1} now has {player1.health} health")
            else:
                print("error")
    elif playerInput == "G":
        print("1. Attack")
        print("2. Heal")
        choice1 = int(input("what do you want Batsigma to help you with?:"))
        if choice1 == 1:
            print("which character do you want to attack")
            print("1. Rizzio")
            print("2. Rizzman")
            print("3. Spiderrizz")
            Attack1 = str(input("Who do you want to attack?:"))
            if Attack1 == "Rizzio":
                if chance >= 3:
                    Rizzio.health -= Batsigma.strength
                    print("Attack sucessful")
                else:
                    Batsigma.health -= Rizzio.strength
                    print("Attack failed")
            elif Attack1 == "Rizzman":
                if chance >= 3:
                    Rizzman.health -= Batsigma.strength
                    print("attack sucessful")
                else:
                    Batsigma.health -= Rizzman.strength
                    print("attack failed")
            elif Attack1 == "Spiderrizz":
                if chance >= 3:
                    Spiderrizz.health -= Batsigma.strength
                    print("attack sucessful")
                else:
                    Batsigma.health -= Rizzman.strength
                    print("attack failed")
            else:
                print("error")
        if choice1 == 2:
            print("which character do you want to heal")
            print("1. Rizzachu")
            print("2.", player1)
            Heal1 = str(input("Who do you want to Heal?:"))
            if Heal1 == "Rizzachu":
                Batsigma.health += Batsigma.rizz
                print("Rizzachu now has", Rizzachu.health, "health")
            elif Heal1 == player1:
                player1.health += Batsigma.rizz
                print( player1, "now has", player1.health, "health")
            else:
                print("error")
    elif playerInput == "H":
        characterChosen = str(input("which charater do you want to check?:"))
        if characterChosen == "Rizzio":
            print(f'{Rizzio.health}')
            print(f'{Rizzio.strength}')
            print(f'{Rizzio.rizz}')
        elif characterChosen == "Rizzman":
            print(f'{Rizzman.health}')
            print(f'{Rizzman.strength}')
            print(f'{Rizzman.rizz}')
        elif characterChosen == "Spidderrizz":
            print(f'{Spiderrizz.health}')
            print(f'{Spiderrizz.strength}')
            print(f'{Spiderrizz.rizz}')
        elif characterChosen == "Rizzachu":
            print(f'{Rizzachu.health}')
            print(f'{Rizzachu.strength}')
            print(f'{Rizzachu.rizz}')
        elif characterChosen == "Batsigma":
            print(f'{Batsigma.health}')
            print(f'{Batsigma.strength}')
            print(f'{Batsigma.rizz}')
        else:
            print("error")
    elif playerInput == "I":
        print("Who do you want to use Rizz on?:")
        print("1. Batsigma")
        print("2. Rizzachu")
        print("3. yourself")
        useRizz = int(input("who do you want to heal:"))
        if useRizz == "1":
            Batsigma.health += player1.rizz
            print(f"Batsigma now has {Batsigma.health} health")
        elif useRizz == "2":
            Rizzachu.health += player1.rizz
            print(f"Rizzachu now has {Rizzachu.health} health")
        elif useRizz == "3":
            player1.health += player1.rizz
            print(f"{player1} now has {player1.health} health")
    elif playerInput == "Q":
        done = bool(True)
        print("you have decided to quit the game")
    else:
        print("error choose again")