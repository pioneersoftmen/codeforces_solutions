t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    penalty = 0
    for char in s:
        if char == '+':
            penalty += 1
        else:
            penalty -= 1
    print(abs(penalty))