t = int(input())
from collections import deque


def solve(n, a):
    if n == 1:
        return 0
    if n == 2:
        if a[0] == a[1]:
            return 0
        return 1
    old = a[0]
    orqa = a[-1]

    if old != orqa:
        q1 = deque(a)
        q2 = deque(a)
        while q1:
            if len(q1) > 0 and q1[0] == old:
                q1.popleft()
            else: break
        while q2:
            if len(q2) > 0 and q2[-1] == orqa:
                q2.pop()
            else: break
        return min(len(q1), len(q2))
    else:
        q = deque(a)
        while len(q) > 0 and q[0] == old:
            if len(q) > 0 and q[0] == old:
                q.popleft()
            else: break
        while len(q) > 0 and q[-1] == orqa:
            if len(q) > 0 and q[-1] == orqa:
                q.pop()
            else:
                break
        return len(q)


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))