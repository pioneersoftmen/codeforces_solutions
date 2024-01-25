t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    xy = []
    for i in range(m):
        x, y = map(int, input().split())
        xy.append([x, y])
    d = {}
    d[0] = 1
    d[n - 1] = n - 2
    for j in range(m):
        cost = 0
        if xy[j][0] < xy[j][1]:
            for k in range(xy[j][0] - 1, xy[j][1] - 1):
                if k in d:
                    if d[k] == k + 1:
                        cost += 1
                    else:
                        cost += abs(a[k] - a[k + 1])
                else:
                    if abs(a[k - 1] - a[k]) < abs(a[k] - a[k + 1]):
                        d[k] = k - 1
                    else:
                        d[k] = k + 1

                    if d[k] == k + 1:
                        cost += 1
                    else:
                        cost += abs(a[k] - a[k + 1])
        else:
            for k in range(xy[j][0] - 1, xy[j][1] - 1, -1):
                if k in d:
                    if d[k] == k - 1:
                        cost += 1
                    else:
                        cost += abs(a[k] - a[k - 1])
                else:
                    if abs(a[k - 1] - a[k]) < abs(a[k] - a[k + 1]):
                        d[k] = k - 1
                    else:
                        d[k] = k + 1

                    if d[k] == k - 1:
                        cost += 1
                    else:
                        cost += abs(a[k] - a[k - 1])
        print(cost)

         