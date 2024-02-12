t = int(input())
def rectangle(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return "NO"
    if a % 2 == 0 and b % 2 == 0:
        return "YES"
    if a > b:
        maximum = a
        minimum = b
    else:
        maximum = b
        minimum = a
    if minimum % 2 == 1 and maximum // 2 == minimum:
        return "NO"
    return "Yes"
    

for _ in range(t):
    a, b = map(int, input().split())
    print(rectangle(a,b))