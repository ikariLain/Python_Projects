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