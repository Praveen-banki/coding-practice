n = 7

for i in range(n):
    # H
    if i == n//2:
        print("* * *", end=" ")
    else:
        print("*   *", end=" ")

    print("   ", end="")

    # I
    if i == 0 or i == n-1:
        print("*****")
    else:
        print("  *")