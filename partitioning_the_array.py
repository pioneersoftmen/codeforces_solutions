import math

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for k in range(1, n + 1):
        if n % k == 0:
            g = 0
            for i in range(n - k):
                g = math.gcd(g, abs(A[i + k] - A[i]))
            ans += (g != 1)
    print(ans)

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()

