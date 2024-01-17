def digit_sum(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits

def number_finder(x, k):
    while digit_sum(x) % k != 0:
        x += 1
    return x


t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    print(number_finder(x, k))