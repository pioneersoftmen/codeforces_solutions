t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n < k //2 or m < k // 2:
        print("NO")
        continue
    seta = set()
    setb = set()
    that = None
    for i in range(min(m, n)):
        if 1 <= a[i] <= k:
            seta.add(a[i])
        if 1 <= b[i] <= k:
            setb.add(b[i])
        if len(seta) + len(setb) >= k and len(seta) >= k // 2 and len(setb) >= k // 2:
            if len(seta | setb) >= k:
                print("YES")
                break
        that = i
    else:
        if len(seta) < k // 2 and len(setb) < k // 2:
            print("NO")
        else:
            if m != n:
                if m > n:
                    if len(seta) < k // 2:
                        print("NO")
                    else:
                        while that < m:
                            if 1 <= b[that] <= k:
                                setb.add(b[that])
                            if len(setb) >= k // 2:
                                if len(seta | setb) >= k and len(seta) >= k // 2 and len(setb) >= k // 2:
                                    print("YES")
                            that += 1
                        else:
                            print("NO")        
                else:
                    if len(setb) < k // 2:
                        print("NO")
                    else:
                        while that <= n:
                            if 1 <= a[that] <= k:
                                setb.add(a[that])
                            if len(setb) >= k // 2:
                                if len(seta | setb) >= k and len(seta) >= k // 2 and len(setb) >= k // 2:
                                    print("YES")
                                    break
                            that += 1
                        else:
                            print("NO")   
                
    