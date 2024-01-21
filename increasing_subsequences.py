import sys
from typing import List

def f(x: int) -> List[int]:
    res = []
    if x == 2:
        res.append(0)
    elif x & 1:
        res = f(x - 1)
        res.append(min(res) - 1)
    else:
        res = f(x // 2)
        res.append(max(res) + 1)
    return res

def main() -> None:
    t = int(input())
    for _ in range(t):
        x = int(input())
        ans = f(x)
        print(len(ans))
        print(*ans)

if __name__ == '__main__':
    main()
