t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    a.append(x)
    distances = [a[j] - a[j - 1] for j in range(1, len(a))]
    max_distance = max(distances)
    ret = 2 * (x - a[-2])
    print(max(max_distance, ret))