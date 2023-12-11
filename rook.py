t = int(input())
s = 'abcdefgh'
d = '12345678'
for i in range(t):
    letter, digit = list(input())
    for j in range(1, 9):
        if str(j) == digit:
            continue
        else:
            print(letter + str(j))

    for p in s:
        if p == letter:
            continue
        else:
            print(p + str(digit)) 