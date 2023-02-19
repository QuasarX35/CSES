n = int(input())
if (n == 1):
    print(1)
    exit()
 
if (n < 4):
    print("NO SOLUTION")
    exit()
 
l2 = list(range(2, n + 1, 2))
l = list(range(1, n + 1, 2))
l2.extend(l)
print(*l2, sep=" ")
