number = int(input("Height of the pyramid : "))
for i in range(1, number + 1):
    for j in range(number - i):
        print(" ", end="")
    for j in range(i * 2 - 1):
        print("*", end="")
    print()

