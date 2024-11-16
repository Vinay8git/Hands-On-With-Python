for i in range(1, 6):
    for space in range(1, 6 - i):
        print(" ", end="")
    for star in range(0, 2 * i - 1):
        print("*", end="")
    print()  # Move to the next line
