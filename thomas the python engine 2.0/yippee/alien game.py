print("welcome to the alien game !")
input("press enter to continue")
print("you have stolen a UFO to make your way across outer space.")
input("press enter to continue")
print("the aliens want their UFO back and are chasing you down !")
input("press enter to continue")
print("survive and out run the alien !")
input("press enter to continue")

print()
print("the rules are:")
print("you must outrun the aileens by more than 150 km")
print("full speed consumes 2 energy points")
print("moderate speed consumes 1 energy point")
print("resting gains 1 energy point, 1 sip of water, and slows you down by 5 kmh")
print("drinking from water bottle uses 1 sip and gains 3 energy points")
print("status check shows how your status")
print("quiting stops the game")
input("press enter to continue")

done = bool(False)

A = "drink from your water bottle."
B = "speed up at full speed"
C = "speed up at moderate speed"
D = "rest"
E = "status check"
Q = "quit"


energyPoints=0

speed = 20 

sips = 3

distance = 10 

print("A.", A)
print("B.", B)
print("C.", C)
print("D.", D)
print("E.", E)
print("Q.", Q)

if distance >= 150:
    done == bool(True)
    print("you won")

if distance <= 0:
    done == bool(True)
    print("you lost")
  

while done == False:
    playerInput=input("choose one:")
    if playerInput == "A":
        print("you gained 3 energy points")
        print("you used", sips, "sips of water")
        energyPoints += 3
        sips -= 1
        print("you have",energyPoints,"energy points")
        print("you have", sips, "sips of water left")
        print("you are", distance, "kmh away from the aliens")
    elif playerInput == "B":
        print("you used 2 energy points to speed up")
        print("your speed has increased by 15 kmh")
        energyPoints -= 2
        speed += 15
        distance += 15
        print("you are travelling at", speed, "kmh")
        print("you now have", energyPoints , "energy points")
        print("you are", distance, "kmh away from the aliens")
    elif playerInput == "C":
        print("you have used 1 energy point to speed up")
        print("your speed as increased by 10 kmh")
        energyPoints -= 1
        speed += 10
        distance += 10
        print("you are travelling at", speed, "kmh")
        print("you now have", energyPoints, "energy points")
        print("you are", distance, "kmh away from the aliens")
    elif playerInput == "D":
        print("you have gained 1 sip of water")
        print("you have gained 1 energy point")
        print("you have slowed down by 5 kmh")
        sips += 1
        energyPoints += 1
        speed -= 5
        distance -= 5
        print("sips:", sips)
        print("you have",energyPoints,"energy points")
        print("you are travelling at", speed, "kmh")
        print("you are", distance, "kmh away from the aliens")
    elif playerInput == "E":
        print("your speed is", speed, "kmh")
        print("you have", energyPoints, "energy points left")
        print("you have", sips, "sips of water left")
        print("you are", distance, "kmh away from the aliens")
    elif playerInput == "Q":
        done = bool(True)
        print("you have decided to quit the game")
    else:
        print("error choose again")



