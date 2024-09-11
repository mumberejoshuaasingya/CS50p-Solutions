import random
import sys


# Prompts the user for a level, n .
level = (input("Level: "))

# If the user does not input a positive integer, the program should prompt again.
while True:
    try:
        if int((level)) > 0:
            break
        else:
            level = (input("Level: "))
    except:
        level = (input("Level: "))
        pass
      

# Randomly generates an integer between 1 and n, inclusive, using the random module.
generated = random.randint(1, int(level))

# Prompts the user to guess that integer. 
Guess = input("Guess: ")


# If the guess is not a positive integer, the program should prompt the user again. 
while True:
    try:
        if int(Guess) > 0:
            if int(Guess) < generated:
                print("Too small!")
                Guess = input("Guess: ")
            elif int(Guess) > generated:
                print("Too large!")
                Guess = input("Guess: ")
            else:
                # print("Just right!")
               break
            # break
    except:
        Guess = input("Guess: ")
        pass
    
print("Just right!")
    # If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    
    # If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    
    # If the guess is the same as that integer, the program should output Just right! and exit.