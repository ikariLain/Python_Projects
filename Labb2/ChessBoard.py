
def EasyMethod():
    print("Welcome to the chessBoard")
    size = input("Enter board size:")
    int_size = int(size)
    for i in range(int_size):
        print()
        for j in range(int_size):
            if (i + j) % 2 == 0:
                print("S", end="")
            else:
                print("W", end="")
    print()

    
def harderMethod():
    print("Welcome to the hard")

switch = {
    "1" : EasyMethod,
    "2" : harderMethod
}   
print("Enter you what kind of cheesboard?")
print("1. Easy method")
print("2. Hard method")
value = input()

selected_method = switch.get(value,lambda : "invalid option")
result = selected_method()

if result:
    print(result)