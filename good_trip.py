M = 10 ** 9 + 7
for tc in range(int(input())):
    n, m, k = map(int, input().split())
    s = 0
    for i in range(m):
        x, y, f = map(int, input().split())
        s += f
    d = pow(n * (n - 1) // 2, M - 2, M)
    p = m * d 
    c = ((k * s) + p * (k * (k - 1)// 2)) % M
    print((c * d) % M)