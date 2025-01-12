import random

easy_random = random.randint(1,20)

print("Welcome! I'm thinking on a number from from 1-20")
print("\nCan you guess it? You have 5 tries")



tries = 5

for attempt  in range(tries):
    
    user_input = int(input(f"Attempt {attempt + 1}/{tries}: Enter your number"))
    
    if user_input == easy_random:
        print("Congratulations! You guessed it!")
        print(f"With only {tries} tries")
        break
    
    elif user_input < easy_random:
        print("Too low! Try again.")
         
    else:
        print("\nYour number is too high! Try again.")
        
# Failed messages
else:
    print("\nSorry, you didn't guess it. The number was", easy_random)