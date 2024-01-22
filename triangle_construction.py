n = int(input())
a = list(map(int, input().split()))

m = max(a)
s = sum(a)

if m > 2 * (s - m):
    print(s - m)
else:
    print(s//3)