from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict(Counter(a))
    length_of_keys = len(list(d.keys()))
    if n == 2:
        print("YES")
        continue
    if length_of_keys < 2:
        print("YES")
    elif length_of_keys == 2:
        value = list(d.values())
        difference = value[1] - value[0]
        if abs(difference) < 2:
            print("YES")
            continue
        else:
            print("NO")
    else:
        print("NO")        
