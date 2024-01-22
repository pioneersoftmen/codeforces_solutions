t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    f = input()
    not_same = 0
    ones = 0
    zeros = 0
    one_f = 0
    zero_f = 0

    for i in range(n):
        if s[i] == '1':
            ones += 1
        else:
            zeros += 1
        if f[i] == '1':
            one_f += 1
        else:
            zero_f += 1
        
        if s[i] != f[i]:
            not_same += 1

    put = abs(ones - one_f)
    not_same -= put

    print(put + not_same // 2)