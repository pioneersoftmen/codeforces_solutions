t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 1
    while n > 0:
        d = n % 10
        n //= 10
        mul = 0
        for i in range(d + 1):
            for j in range(d + 1):
                if d - i - j >= 0:
                    mul += 1
        cnt *= mul
    print(cnt)