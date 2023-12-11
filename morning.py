t = int(input())
for i in range(t):
    n = input()
    digits = list(n)

    for k in range(len(digits)):
        if digits[k] == '0':
            digits[k] = '10'
    digits.insert(0, 1)

    arr = [abs(int(digits[i]) - int(digits[i - 1])) for i in range(1, len(digits))]
    print(sum(arr) + 4)