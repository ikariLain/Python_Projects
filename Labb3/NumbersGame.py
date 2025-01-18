import random

def deafult():
    easy_random = random.randint(1,20)

    print("Welcome! I'm thinking on a number from from 1-20")
    print("\nCan you guess it? You have 5 tries")

    tries = 5

    for attempt in range(tries):
    
        user_input = int(input(f"\nAttempt {attempt + 1}/{tries}: Enter your number: "))
    
        if user_input == easy_random:
            print("Congratulations! You guessed it!")
            print(f"With only {attempt} tries")
            break
    
        elif user_input < easy_random:
            print("\nToo low! Try again.")
         
        else:
            print("\nYour number is too high! Try again.")
        
# Failed messages
    else:
        print("\nSorry, you didn't guess it. The number was", easy_random)

def pick_your_number():
    while True:
        start_value = int(input("\nEnter your start number: "))
        end_value = int(input("\nEnter your end number: "))
        tries = int(input("\nHow many tries do you need? "))
        
    
        if end_value < start_value:
                print("\nInvalid input, the start nummber is to high")
                return 
        else:
            break
        
    rank2_random = random.randint(start_value, end_value)
    
    #Depending on the user input get an extra message    
    def variation_respone(user_input):
        if (user_input - rank2_random) <=5:
            return("Wow! your real close You are close!")
            
        elif (user_input - rank2_random) <=10:
            return("You are within you are getting closer!")
            
        elif (user_input - rank2_random) <=60:
            return("You can do better!  :)  ")
            
        else:
            return("\nYou are not even close!  :/  ")

    for attempt  in range(tries):
    
        user_input = int(input(f"\nAttempt {attempt + 1}/{tries}: Enter your number: "))
    
        if user_input == rank2_random:
            print("\nCongratulations! You guessed it!")
            print(f"\nWith only {attempt} tries")
            break
            
        elif user_input < rank2_random:
            print(f"\nToo low! Try again {variation_respone(user_input)}")
        
        else:
            print(f"\nYour number is too high! Try again {variation_respone(user_input)}")
            
    # Failed messages
    else:
        print(f"\nSorry, you didn't guess it. The number was {rank2_random}")
        
#Switch function
def switch(choice):
    
    switch = {
        1: deafult,
        2: pick_your_number,
    }
    return switch.get(choice, deafult)()

#Main function
def Main():
    while True:
        print("Welcome to guess the number!")
        print("1. Easy mode")
        print("2. Pick your own number")
        print("3. Exit")
        
        choice = int(input("\nEnter your choice: "))
        if choice == 1 or choice == 2:
            print(switch(choice))
        elif choice == 3:
            print("\nThank you for playing!")
            break
        else:
            print("\nInvalid input, please try again")

        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("\nThank you for playing!")
            break
        
#Start the game
Main()