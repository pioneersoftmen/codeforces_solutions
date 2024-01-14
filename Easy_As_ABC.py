arr = []
for _ in range(3):
    arr.append(input())
small = 'CCC'
for i in range(3):
    for j in range(3):
        s = arr[i][j]
        for k in range(3):
            for l in range(3):
                if (k == i - 1 or k == i + 1) and (l == j - 1 or l == j + 1):
                    s += arr[k][l]
                for m in range(3):
                    for n in range(3):
                        if (m == k - 1 or m == k + 1) and (n == l - 1 or n == l + 1) and (m != i and n != j):
                            s += arr[m][n]
                        if s < small and len(s) == 3:
                            small = ''.join(sorted(list(s)))
                            print([i, j], [k, l], [m, n])
                        if small == 'AAA':
                            print('AAA')
                            exit()
print(small)