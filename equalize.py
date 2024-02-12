from bisect import bisect_right as bl
for _ in range(int(input())):
    n = int(input())
    lis = sorted(set(map(int, input().split())))
    mx = -1
    cur = 0
    for i in lis:
        mx = max(mx, bl(lis, i + n - 1) - cur)
        cur += 1
    print(mx)
