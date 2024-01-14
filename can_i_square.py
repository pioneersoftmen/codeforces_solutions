from math import sqrt
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    summa = sum(a)
    if sqrt(summa) == int(sqrt(summa)):
        print("Yes")
    else:
        print("No")