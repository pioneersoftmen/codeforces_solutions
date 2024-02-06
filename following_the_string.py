from string import ascii_lowercase
t = int(input())

for _ in range(t):
    n = int(input())
    alphabet = ascii_lowercase
    j = 0
    d = {}
    s = ""
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i] == 0:
            if a[i] in d:
                d[a[i]].append(alphabet[j])
            else:
                d[a[i]] = [alphabet[j]]                       
            s += alphabet[j]
            j += 1
        else:
            letter = d[a[i] - 1].pop()
            s += letter
            if a[i] in d:
                d[a[i]].append(letter)
            else:
                d[a[i]] = [letter]
    print(s)
            

