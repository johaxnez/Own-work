
import random
#from number_guess_art import logo
NUMBER = random.choice(range(1, 101))
user_wins = False

logo = """
###  ##  ##  ###  ##   ##  ### ##   ### ###  ### ##             ## ##   ##  ###  ### ###   ## ##    ## ##   ### ###  ### ##   
  ## ##  ##   ##   ## ##    ##  ##   ##  ##   ##  ##           ##   ##  ##   ##   ##  ##  ##   ##  ##   ##   ##  ##   ##  ##  
 # ## #  ##   ##  # ### #   ##  ##   ##       ##  ##           ##       ##   ##   ##      ####     ####      ##       ##  ##  
 ## ##   ##   ##  ## # ##   ## ##    ## ##    ## ##            ##  ###  ##   ##   ## ##    #####    #####    ## ##    ## ##   
 ##  ##  ##   ##  ##   ##   ##  ##   ##       ## ##            ##   ##  ##   ##   ##          ###      ###   ##       ## ##   
 ##  ##  ##   ##  ##   ##   ##  ##   ##  ##   ##  ##           ##   ##  ##   ##   ##  ##  ##   ##  ##   ##   ##  ##   ##  ##  
###  ##   ## ##   ##   ##  ### ##   ### ###  #### ##            ## ##    ## ##   ### ###   ## ##    ## ##   ### ###  #### ##  
                                                                                                                            
                                                                                                                        """
                                                                                                                        
def user_guess(NUMBER, lives, user_number):
    if user_number == NUMBER:
        print(f"You guessed {user_number}. This is correct. You win!")
        user_wins = True
        return user_wins
    elif user_number > NUMBER:
        print(f"You guessed {user_number}. To high.")
        
    else:
        print(f"You guessed {user_number}. To low.")
        
def new_guess(user_number, lives):
    print(f"You have {lives} lives left.")
    user_number = int(input("Guess a number between 1 and 100: "))
    return user_number


def remove_life(user_number, lives):
    if user_number != NUMBER:
        lives -= 1
    return lives

# game starts here:
print(logo)

difficulty = input("Do you want the 'easy' or 'hard' difficulty?: ").lower()

if difficulty == "hard":
    lives = 5
else:
    lives = 10
    

user_number = int(input("Guess a number between 1 and 100: "))
while lives > 0 and user_number != NUMBER:
    print(NUMBER)
    user_guess(NUMBER, lives, user_number)
    lives = remove_life(user_number, lives)
    user_number = new_guess(user_number, lives)

    if lives == 0:
        print("Sorry, you ware out of lives.")
        break
    if user_number == NUMBER:
        print(f"Hooray! You guessed the right number, {NUMBER}. ")
        input("Type enter to exit.")
        break
        




