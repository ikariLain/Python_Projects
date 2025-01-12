
def EasyMethod():
    print("Welcome to the easier method")
    size = input("Enter board size:")
    int_size = int(size)
    for i in range(int_size):
        print()
        for j in range(int_size):
            if (i + j) % 2 == 0:
                print("W", end="")
            else:
                print("B", end="")
    print()

def Print_grid(grid):
        for row in grid:
            print(" ".join(row)) 
    
def harderMethod():
    
    print("Welcome to the harder method")
    print("Press max size 64")
    size = input("Enter board size:")
    
    if int(size) > 64:
        print("Size too large, max size 64")
        return

    # Get the needed symbols from user
    symbol1 = input("Enter symbol for white pieces: ")
    symbol2 = input("\nEnter symbol for black pieces: ")
    int_size = int(size)
    
    
    grid = [[""for _ in range(int_size)] for _ in range(int_size)]
    for i in range(int_size):
        for j in range(int_size):
                grid[i][j] = symbol1 if(i+j) % 2 == 0 else symbol2
                
    #Print out grid
    print("\nInitial Chessboard")
    Print_grid(grid)
    
    # Allow to make custom symbols dynamically
    while True:
        print("\nWould you like to modify the chessboard? [Y/N]")
        choice = input().lower()
        if choice == "n":
            break
        
        # Get coordinates    
        x = int(input("Enter x coordinate (row):  "))
        y = int(input("Enter y coordinate (column): "))
        custom_symbol = input("Enter symbol: ")
    
        if 0 <= x < int_size and 0 <= y < int_size:
            grid[x][y] = custom_symbol
        else:
            print("Invalid coordinates")
        
        print("\nUpdated chessboard:")
        Print_grid(grid)
        
    print("\nFinal Chessboard")
    Print_grid(grid)
        
           
        
            

switch = {
    "1" : EasyMethod,
    "2" : harderMethod
}   
print("Welcome to the chessBoard")
print("Enter you what kind of cheesboard?")
print("1. Easy method")
print("2. Hard method")
value = input()

selected_method = switch.get(value,lambda : "invalid option")
result = selected_method()

if result:
    print(result)