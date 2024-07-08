def getUserInput(userIn):
    return userIn

def boldText(text):
    text+='*'
    return text

def printing(w):
    for i in range(0,len(w)):
        for k in range(0,5):
            print(f" {w[i][k]}",end='')
        print("\n")

print("welcome to wordle\n")

userIn=[
    ["|-|","|-|","|-|","|-|","|-|"],
    ["|-|","|-|","|-|","|-|","|-|"],
    ["|-|","|-|","|-|","|-|","|-|"],
    ["|-|","|-|","|-|","|-|","|-|"],
    ["|-|","|-|","|-|","|-|","|-|"],
    ["|-|","|-|","|-|","|-|","|-|"],

]

wordleWord="adieu"
for s in range(0,6):
    printing(userIn)
    player=str(input("guess a word:"))
    userIn[s][0]=" "+player[0]+" "
    userIn[s][1]=" "+player[1]+" "
    userIn[s][2]=" "+player[2]+" "
    userIn[s][3]=" "+player[3]+" "
    userIn[s][4]=" "+player[4]+" "

    if wordleWord==player:
        print("yay you did it")
    elif player!=wordleWord:
        for q in range(0,5):
            if player[q]==wordleWord[q]:
                userIn[s][q]==player[q].upper()
            elif player[q] in wordleWord:
                userIn[s][q]=player[q]+"*"