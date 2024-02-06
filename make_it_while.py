t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    first, second = None, None
    for i in range(len(s)):
        if s[i] == 'B':
            first = i
            break
    for j in range(len(s) - 1, -1, -1):
        if s[j] == "B":
            second = j
            break
    if first == None and second == None:
        print(0)
    else:
        print(second - first + 1)