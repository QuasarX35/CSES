n = int(input())
print(str(n), end=" ")
while (n != 1):
    if (n % 2 == 0):
        n /= 2
        print(str(int(n)), end=" ")
    else:
        n *= 3
        n += 1
        print(str(int(n)), end=" ")
