t = int(input())

def yes_or_no(n):
    for x in range(1, 3):
        for y in range(2, 6):
            if y == 3 or x == y:
                continue
            z = n - x - y
            if z % 3 != 0 and z != x and z != y:
                return "YES\n{} {} {}".format(x, y, z)
    return "NO"

for _ in range(t):
    n = int(input())
    if n < 7:
        print("NO")
        continue
    print(yes_or_no(n))

        
