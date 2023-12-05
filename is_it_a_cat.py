import re
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    example = r'^[mM]+[eE]+[oO]+[wW]+$'
    if re.match(example, s):
        print('YES')
    else:
        print('NO')