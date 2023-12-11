for i in range(int(input())):
    a = list(map(int, input().split()))
    count = 0
    for j in range(1, len(a)):
        if a[0] < a[j]:
            count += 1
        
    print(count) 