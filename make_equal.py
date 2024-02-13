t = int(input())


def solve(n, a):
    if n == 1:
        return ("YES")
    average = sum(a) // n
    zapas = 0
    for i in range(n):
        if a[i] == average:
            continue
        elif a[i] > average:
            zapas += a[i] - average
        else:
            if a[i] < average:
                if zapas < average - a[i]:
                    return ("NO")
                    
                if zapas >= average - a[i]:
                    zapas -= average - a[i]
    return "yes"

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

    