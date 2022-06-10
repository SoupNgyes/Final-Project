import random

pcInp = random.randint(0, 2)

play = True

def game():
  global pcInp
  pcInp = random.randint(0,2)
  if pcInp == 0:
    pcInp = "rock"
  
  if pcInp == 1:
    pcInp = "paper"
  
  if pcInp == 2:
    pcInp = "scissors"
  
  
  
  uInp = input("Rock, paper, or scissors?: ")
  
  print(f"I chose: {pcInp}")
  
  if uInp == "rock" and pcInp == "paper":
    
    print("You Lose")
    
    
  elif uInp == "paper" and pcInp == "scissors":
    
    print("You Lose!")
    
    
  elif uInp == "scissors" and pcInp == "rock":
    
    print("You Lose!")
    
  elif uInp == "rock" and pcInp == "rock":
    
    print("Tie!")
    
    
  elif uInp == "paper" and pcInp == "paper":
    
    print("Tie!")
    
    
  elif uInp == "scissors" and pcInp == "scissors":
    
    print("Tie!")
    
    
  elif uInp == "paper" and pcInp == "rock":
    
    print("WIN!")
    
    
  elif uInp == "rock" and pcInp == "scissors":
    
    print("WIN!")
    
    
  elif uInp == "scissors" and pcInp == "paper":
    
    print("WIN!")
  
  
game()
while play == True:
  again = input("Try Again? Y/N: ")
  if again == "Y":
    game()    
      
  elif again == "N":
    print("Goodbye")
    break

