t = int(input())
for _ in range(t):
    n = int(input())
    d = []
    interval = [0, float('inf')]
    ak = []
    for i in range(n):
        a = list(map(int, input().split()))
        ak.append(a)

    for j in range(len(ak)):
        if ak[j][0] == 1:
            if interval[0] < ak[j][1]:
                interval[0] = ak[j][1]
        elif ak[j][0] == 2:
            if interval[1] > ak[j][1]:
                interval[1] = ak[j][1]
        elif ak[j][0] == 3:
            d.append(ak[j][1])
    count = 0

    for k in d:
        if k >= interval[0] and k <= interval[1]:
            count += 1
    
    print(max(interval[1] - interval[0] - count + 1, 0))
