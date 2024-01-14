t = int(input())

for _ in range(t):
    a, b, c = list(map(int, input().split()))
    a_parity = a % 2
    b_parity = b % 2
    c_parity = c % 2
    arr = []
    if a_parity == b_parity == c_parity:
        for i in range(3):
            arr.append(1)
    elif a_parity == b_parity:
        arr.append(0)
        arr.append(0)
        arr.append(1)
    elif a_parity == c_parity:
        arr.append(0)
        arr.append(1)
        arr.append(0)
    else:
        arr.append(1)
        arr.extend([0, 0])
    print(*arr)