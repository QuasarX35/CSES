n = (input())
l = [int(x) for x in input().split()]

t = 0
for i in range(1, len(l)):
    if l[i] < l[i - 1]:
        d = l[i - 1] - l[i]
        l[i] += d
        t += d

print(t)