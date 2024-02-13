from string import ascii_lowercase

t = int(input())
for i in range(t):
    n = int(input())
    word = ''
    while n >= 28:
        word += 'z'
        n -= 26
    if len(word) == 2:
        word += ascii_lowercase[n - 1]
    elif len(word) == 1:
        word += 'a'
        n -= 1
        word += ascii_lowercase[n - 1]
    elif len(word) == 0:
        word += 'aa'
        n -= 2
        word += ascii_lowercase[n - 1]
    print(''.join(sorted(word)))
