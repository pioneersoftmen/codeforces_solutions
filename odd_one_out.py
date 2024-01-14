from collections import defaultdict
t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(len(arr)):
        d[arr[i]] += 1
    for key in d.keys():
        if d[key] == 1:
            print(key)