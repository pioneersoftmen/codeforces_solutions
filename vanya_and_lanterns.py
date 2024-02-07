n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
maximum = -1
for i in range(1, n):
    maximum = max(maximum, a[i] - a[i - 1])
first = a[0] - 0
second = l - a[-1]
print(max(maximum / 2, first, second))