from math import log2
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(1, n):
        b.append(a[i] - a[i - 1])
    for i in range(1, len(b) + 1):  

        if not log2(i).is_integer() and b[i - 1] < 0:
            print('NO')
            break
    else:
        print('YES')