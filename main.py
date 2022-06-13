from random import random
from random import choice


R = "rock"
P =  "paper" 
S = "scissors"

gameoptions = [R, S, P]
print("Enter your option:")
# cpu = random.choice(gameoptions)
cpu = "you"
player = input()
for i in gameoptions:
    if i == R:
        print(i ,":", cpu)
    
    elif i == S:
        
        print(i)
    elif i == P:
        print(i)
    else:
        print("not amongst our options")

         



             
