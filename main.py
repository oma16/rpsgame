from random import random

while True:
    rock = "R"
    paper =  "P" 
    scissors = "S"

    gameoptions = [rock, paper, scissors]
    computeroption = random.choice(gameoptions)
    player = input("Enter your option(R or S or P):").upper()
    if player in gameoptions:
        print(f"\nplayer {player} : cpu {computeroption}")
       
    else:  
         print("not amongst our options")  
        
    if player == computeroption:
            print("both player selected {player}. it is a tie")
        
    elif player == rock:
        if  computeroption == scissors:
            print("Rock smahes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose")    

    elif player == paper:
        if  computeroption == rock:
            print("Paper covers Rock! You win") 
            
        else:
            print("Scissors cuts paper! You lose!")
    elif player == scissors:
        if  computeroption == paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes Scissors! You lose")    

    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
       break
         



             
