l = [x for x in input()]
n, b = 1, 1
for i in range(1, len(l)):
    if l[i] == l[i - 1]:
        n += 1
        if (b < n):
            b = n
    else:
        n = 1
print(b)
