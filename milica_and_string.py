from collections import defaultdict
t = int(input())


for _ in range(t):
    a = 0
    b = 0
    d = defaultdict(int)
    n, k = map(int, input().split())
    s = input()
    for c in range(len(s)):
        if s[c] == 'A':
            a += 1
        else:
            b += 1
        d[c + 1] = [a, b]
    
    if b == k:
        print(0)
        continue
    for i in range(n):
        if b - (d[i + 1][1]) == k:
            print(1)
            print(i + 1, 'A')
            break
        elif i + 1 + b - (d[i + 1][1]) == k:
            print(1)
            print(i + 1, "B")
            break
    else:
        print(2)
        print(n, "A")
        print(k, "B")
