n = int(input())
a = list(map(int, input().split()))
a.append(a[0])
height = float('inf')
b = []
for i in range(1, len(a)):
    if abs(a[i] - a[i - 1]) < height:
        b = [i, i - 1]
        height = abs(a[i] - a[i - 1])
if b[0] == n:
    b[0] = 1
    b[1] = n 
else:
    b[0] = b[0] + 1
    b[1] = b[1] + 1
print(*b)

