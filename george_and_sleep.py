s = input()
t = input()
bed = [0] * 2

s = s.split(':')
t = t.split(':')

s = list(map(int, s))
t = list(map(int, t))

if s[1] >= t[1]:
    bed[1] = s[1] - t[1]
else:
    bed[1] = s[1] + 60 - t[1]

if s[0] >= t[0]:
    bed[0] = s[0] - t[0]
else:
    bed[0] = s[0] + 24 - t[0]
bed = list(map(str, bed))
if len(bed[1]) == 1:
    bed[1] = '0' + bed[1]
if len(bed[0]) == 1:
    bed[0] = '0' + bed[0]


print(":".join(bed))
    
