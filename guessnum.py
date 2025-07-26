import random
def number_guess_game():
    number_guess=random.randint(1,100)
    attempt=0
    print("welcome to number guessing game!")
    print(" I am thinking a number between 1 and 100,now its ur turn to guess")
    while True:
        try:
            guess=int(input("enter num:"))
            attempt+=1
            if guess<number_guess:
                print("too low,try again")
            elif guess>number_guess:
                print("too high ,try again")
            else:
                print("hurray ur guess is matched")
        except ValueError:
            print("invalid try again")
number_guess_game()

            
            
