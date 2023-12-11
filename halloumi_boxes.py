t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if a == sorted(a) or k > 1:
        print('YES')
    else:
        print('NO')
    