t = int(input())
for _ in range(t):
    arr = []
    a1 = sum(list(map(int, input().split())))
    a2 = sum(list(map(int, input().split())))
    arr.append(a1)
    arr.append(a2)
    sum_arr = sum(arr)
    if sum_arr == 4:
        print(2)
    elif sum_arr > 0:
        print(1)
    else:
        print(0)