t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = a[:n]
    y = a[n:]
    result = list(zip(x,y))
    distance = 0
    for j in range(1, len(result)):
        distance += result[j][0] -result[j - 1][0]
        distance += result[j][1] - result[j - 1][1]

    print(distance)
    for d in result:
        print(d[0], d[1], sep=' ')