for _ in range(int(input())):
    n = int(input())
    l = [*map(int, input().split())]
    a = l[-1]
    r = 0
    for i in range(n - 2, -1, -1):
        x = (l[i] + a - 1) // a
        r += x - 1
        a = l[i] // x
    print(r)
