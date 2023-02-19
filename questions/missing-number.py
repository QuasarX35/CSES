t, t2 = 0, 0
n = int(input())
l = [int(x) for x in input().split()]
for i in range(n + 1):
    t += i
for i in l:
    t2 += i
print(t - t2)
