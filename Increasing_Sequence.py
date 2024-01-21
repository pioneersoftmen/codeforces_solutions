t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    if a[0] == 1:
        b.append(2)
    else:
        b.append(1)

    for i in range(1, n):
        if a[i] == b[i - 1] + 1:
            b.append(b[i - 1] + 2)
        else:
            b.append(b[i - 1] + 1)

    print(b[-1])   