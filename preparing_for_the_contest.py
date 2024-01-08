t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = []
    q = k
    for m in range(1, k + 1):
        if q == 0:
            break
        arr.append(q)
        q -= 1


    p = k
    for n in range(1, k +  1):
        if n - p + 1 == n:
            break
        arr.append(n - p + 1)
        p += 1
        
    r = k
    for b in range(k + 1, n - k + 1):
        if n - r + 1 == n - k + 1:
            break
        arr.append(r + 1)
        r += 1
    print(arr)
