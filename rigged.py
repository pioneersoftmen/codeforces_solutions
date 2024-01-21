t = int(input())
 
for _ in range(t):
    n = int(input())
    s = []
    e = []
    for i in range(n):
        si, ei = map(int, input().split())
        s.append(si)
        e.append(ei)
    polycarp_endurance = e[0]
    if all(polycarp_endurance > e[j] for j in range(1, len(e)) if s[j] >= s[0]):
        print(s[0])
    else:
        print(-1)