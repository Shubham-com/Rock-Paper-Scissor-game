#Algorithm
'''
Print the Game Instruction to the User/Player
    
Infinite Loop 
    Tell User to enter either Rock, Paper, Scissor
    Get the response from the User
    Print the response from the User
    
    Computer chooses randomly between Rock, Paper and Scissor
    Print computers choice
    Print User Choice and Computer Choice
    
    
    Decide the condition of wining according to the Game Instructions
    
    
    Compare the result with user and computer 
    Printing either user or computer wins 
    
    
    Get the response from User to Play Again
    Check the response from User and continue the loop
    Othewise break the loop to close the game
Print a Thanks Message to the user

'''

#Rock , Paper , Scissor Game

print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                                +"\tRock  vs paper   -> paper wins \n"
                                +"\tRock  vs scissor -> Rock wins \n"
                                +"\tpaper vs scissor -> scissor wins \n") 

while True:

        
    print("Enter choice \n 1. rock \n 2. paper \n 3. scissor \n") 
      
    while True:
        user_choice = input("User turn: > ") 
        user_choice = user_choice.lower()
        
        if user_choice not in ['rock','paper','scissor']:
                print ("Wrong input, please input again: ")
        else:
            break
    
    print("User has choosen : " + user_choice + "\n") 
    

    
    import random
    comp_choice = random.choice(['rock','paper','scissor']) 
    
    # choice function can often be used for choosing a random element from a list.

    print("Computer choice is: " + comp_choice + "\n") 
  
    print("\t" + user_choice + "\n V/s \n" + "\t"+ comp_choice) 
    

    result = None
    
    if((user_choice == "rock" and comp_choice == "paper") or
      (user_choice == "paper" and comp_choice == "rock" )): 
        result = "paper"
    elif((user_choice == "rock" and comp_choice == "scissor") or
        (user_choice == "scissor" and comp_choice == "rock")): 
        result = "rock"
     elif((user_choice == "scissor" and comp_choice == "paper") or
        (user_choice == "paper" and comp_choice == "scissor")): 
        result = "paper"  
    elif(user_choice == "rock" and comp_choice == "rock"):
        result = "rock"
    elif(user_choice == "paper" and comp_choice == "paper"): 
        result = "paper"
    elif(user_choice == "scissor" and comp_choice == "scissor"): 
       result = "scissor"
    else: 
        result = "scissor"
    

    if (result == user_choice and result == comp_choice): 
        print("<== Draw ==>") 
    elif (result == user_choice): 
        print("<== User wins ==>") 
    else: 
        print("<== Computer wins ==>") 
    
      
    ans = input("Do you want to play again ? (Y/N) > ") 
  
    if (ans == 'n' or ans == 'N') : 
        break

print("\nThanks for playing Rock Paper Scissor Game \n") 
