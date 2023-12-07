t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = [0] * n
    for i in range(0, n, 2):
        new_arr[i] = -arr[i + 1]
        new_arr[i + 1] = arr[i]
    print(new_arr)