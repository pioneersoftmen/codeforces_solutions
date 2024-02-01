n = int(input())
d = {}
for _ in range(n):
    s = input()
    if s in d:
        new_name = s + str(d[s])
        print(new_name)
        d[new_name] = 1
        d[s] += 1
    else:
        d[s] = 1
        print("OK")
