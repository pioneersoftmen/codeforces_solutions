t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mna = min(a)
    mnb = min(b)
    summa_a = sum(element + mnb for element in a)
    summa_b = sum(element + mna for element in b)
    print(min(summa_a, summa_b))
