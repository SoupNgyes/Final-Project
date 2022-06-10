import random

pcInp = random.randint(0, 2)
pcWin = 0
userWin = 0
win = False
play = True

if pcInp == 0:
  pcInp = "rock"

if pcInp == 1:
  pcInp = "paper"

if pcInp == 2:
  pcInp = "scissors"


while play == True:
  while win == False:
    uInp = input("Rock, paper, or scissors?: ")

    if uInp == "rock" and pcInp == "paper":
      win = False
      print("You Lose")
      
    elif uInp == "paper" and pcInp == "scissors":
      win = False
      print("You Lose!")
    elif uInp == "scissors" and pcInp == "rock":
      win = False
      print("You Lose!")
      
    elif uInp == "rock" and pcInp == "rock":
      win = False
      print("Tie!")
      
    elif uInp == "paper" and pcInp == "paper":
      win = False
      print("Tie!")
    elif uInp == "scissors" and pcInp == "scissors":
      win = False
      print("Tie!")
    


  if win == False:
    
    again = input("Would you like to play again? Y/N: ")  
  if again == "Y":
    tries = 5
    pcInp = random.randint(0, 3)
  elif again == "N":
    print("Goodbye")
    play = False

