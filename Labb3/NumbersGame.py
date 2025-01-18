import random


def deafult():
    easy_random = random.randint(1,20)

    print("Welcome! I'm thinking on a number from from 1-20")
    print("\nCan you guess it? You have 5 tries")



    tries = 5

    for attempt in range(tries):
    
        user_input = int(input(f"Attempt {attempt + 1}/{tries}: Enter your number"))
    
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
        start_value = int(input("Enter your start number"))
        end_value = int(input("Enter your end number"))
        tries = int(input("How many tries do you need?"))
        
    
        if end_value < start_value:
                print("Invalid input, the start nummber is to high")
                return 
        else:
            break
        
    rank2_random = random.randint(start_value, end_value)

    for attempt  in range(tries):
    
        user_input = int(input(f"Attempt {attempt + 1}/{tries}: Enter your number"))
    
        if user_input == rank2_random:
            print("Congratulations! You guessed it!")
            print(f"With only {attempt} tries")
            break
    
        elif user_input < rank2_random:
            print("\nToo low! Try again.")
         
        else:
            print("\nYour number is too high! Try again.")
        
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