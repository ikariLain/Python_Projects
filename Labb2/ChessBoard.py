
def EasyMethod():
    print("Welcome to the easier method")
    size = input("Enter board size:")
    int_size = int(size)
    for i in range(int_size):
        print()
        for j in range(int_size):
            if (i + j) % 2 == 0:
                print("S", end="")
            else:
                print("B", end="")
    print()

    
def harderMethod():
    print("Welcome to the harder method")
    print("Press max size 64")
    size = input("Enter board size:")
    if int(size) > 64:
        print("Size too large, max size 64")
        return
    else:
        symbol1 = input("Enter symbol for white pieces: ")
        symbol2 = input("Enter symbol for black pieces: ")
        int_size = int(size)
        for i in range(int_size):
            print()
            for j in range(int_size):
                if (i + j) % 2 == 0:
                    print(f"{symbol1}", end="")
                else:
                    print(f"{symbol2}", end="")
    print()
    
    

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