import math
A, B = map(int, input().split())
if A <= B:
    print(math.factorial(A))
else:
    print(math.factorial(B))