t = int(input())
for _ in range(t):
    a, b, c = sorted(map(int, input().split()))
    if a == b and b == c:
        print('yes')
    else:
        if b % a != 0 or c % a != 0:
            print('no')
        else: 
            if (b / a + c / a - 2) <= 3:
                print('yes')
            else:
                print('no')