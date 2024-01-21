t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()
    if s in x:
        print(0)
        continue
    for i in range(1, 6):
        x += x
        if s in x:
            print(i)
            break
    else:
        print(-1)
