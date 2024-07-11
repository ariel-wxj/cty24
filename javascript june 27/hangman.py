print("welcome to my hangman")
secretword="entertainment"

# print(unicorn)
 
HANGMAN= [
     
"____\n|/   |\n|\n|\n|\n|\n|\n|_____\n",
'''
 ______
 |/   |
 |   (_)
 |
 |    
 |    
 |
 |_____
 ''',

 '''___
 |/   |
 |   (_)
 |    |
 |    |    
 |    
 |
 |_____'''
 ,

 '''____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____'''
,

'''___
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____'''
,

 '''_
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____'''
,
'''___
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____'''
,
'''____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____'''
]

wrongGuess=0
guessword= "what you guess"
for i in range (0,7):
 playerinput=input("guess a letter")
 if playerinput not in secretword:
    wrongGuess+=1
    print(HANGMAN[wrongGuess])
 else:
    print(HANGMAN[wrongGuess])
    pass
 
 if guessword == secretword:
   print("congratulations")

   