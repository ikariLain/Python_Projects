import random

def deafult():
    easy_random = random.randint(1,20)

    print("Welcome! I'm thinking on a number from from 1-20")
    print("\nCan you guess it? You have 5 tries")

    tries = 5

    for attempt in range(tries):
    
        user_input = int(input(f"Attempt {attempt + 1}/{tries}: Enter your number: "))
    
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
        if (user_input - rank2_random) <=10:
            return("\nWow! your real close You are close!")
            
        elif (user_input - rank2_random) <=20:
            return("\nYou are within you are getting closer!")
            
        elif (user_input - rank2_random) <=60:
            return("\nYou can do better!  :)  ")
            
        else:
            return("\nYou are not even close!  :/  ")

    for attempt  in range(tries):
    
        user_input = int(input(f"Attempt {attempt + 1}/{tries}: Enter your number"))
    
        if user_input == rank2_random:
            print("\nCongratulations! You guessed it!")
            print(f"\nWith only {attempt} tries")
            break
            
        elif user_input < rank2_random:
            print("\nToo low! Try again.")
            print(variation_respone(user_input))
        
        else:
            print("\nYour number is too high! Try again.")
            print(variation_respone(user_input))
            
    # Failed messages
    else:
        print("\nSorry, you didn't guess it. The number was", rank2_random)
        
def switch(choice):
    
    switch = {
        1: deafult,
        2: pick_your_number,
    }
    return switch.get(choice, deafult)()

print("Welcome to guess the number!")
choice = int(input("Enter your choice"))
print(switch(choice))