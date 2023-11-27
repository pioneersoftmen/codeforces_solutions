t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input()
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    number_of_odds = 0
    for key in d.keys():
        if d[key] % 2 == 1:
            number_of_odds += 1
    if number_of_odds > k + 1:
        print('NO')
    else:
        print('Yes')