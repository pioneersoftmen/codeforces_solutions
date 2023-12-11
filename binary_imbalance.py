t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    for j in range(n):
        if s[j] == '0':
            print('YES')
            break
        if j == n - 1:
            print('NO')