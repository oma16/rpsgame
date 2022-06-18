from random import Random

while True:
    R = "rock"
    P =  "paper" 
    S = "scissors"

    gameoptions = [R, S, P]
    computeroption = Random.choice(gameoptions)
    player = input("Enter your option(R or S or P):")
    if player == (R or S or P):
        print(f"\nplayer {player} : cpu {computeroption}")
       
    else:  
         print("not amongst our options")  
        
    if player == computeroption:
            print("both player selected {player}. it is a tie")
        
    elif player == R:
        if  computeroption == S:
            print("Rock smahes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose")    

    elif player == P:
        if  computeroption == R:
            print("Paper covers Rock! You win") 
            
        else:
            print("Scissors cuts paper! You lose!")
    elif player == S:
        if  computeroption == P:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes Scissors! You lose")    

    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
       break
         



             
