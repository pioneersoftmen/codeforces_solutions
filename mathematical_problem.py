def solve():
    N = int(input())
    if N == 1:
        print(1)
        return
    else:
        s = []
        for b in range(1, N//2 + 1):
            s.append("1" + "0"*(b-1) + "6" + "0"*(b-1) + "9" + "0"*(N - 2*b - 1))
            s.append("9" + "0"*(b-1) + "6" + "0"*(b-1) + "1" + "0"*(N - 2*b - 1))
        s.append("196" + "0"*(N-3))
        s = s[:N]
        for x in s:
            print(x)

T = int(input())
while T > 0:
    solve()
    T -= 1