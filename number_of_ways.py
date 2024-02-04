from collections import defaultdict

a = [0] * 1000010
cnt = defaultdict(int)

def main():
    n = int(input())

    a = list(map(int, input().split()))
    s = sum(a)
    if s % 3 != 0:
        print("0")
    else:
        s //= 3
        ss = 0
        for i in range(n-1, -1, -1):
            ss += a[i]
            if ss == s:
                cnt[i] = 1
        for i in range(n-2, -1, -1):
            cnt[i] += cnt[i+1]
        ans = 0
        ss = 0
        for i in range(n-2):
            ss += a[i]
            if ss == s:
                ans += cnt[i+2]
        print(ans)

if __name__ == "__main__":
    main()

