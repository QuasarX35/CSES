n = int(input())
l = []
for i in range(n):
    y, x = [int(i) for i in input().split()]
    y -= 1
    x -= 1
    if y >= x:
        # if y is even
        if y % 2 == 0:
            t = (y**2) + 1 + x
        # if y is odd
        else:
            t = (y + 1)**2 - x
    else:
        # if x is even
        if x % 2 == 0:
            t = (x + 1)**2 - y
        # if x is odd
        else:
            t = x**2 + 1 + y
    l.append(t)

for i in l:
    print(i)
