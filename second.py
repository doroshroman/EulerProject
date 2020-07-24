# https://projecteuler.net/problem=2

limit = 4 * 10**6
first, second = 1, 2
fibonacci_numbers = [first, second]
sum = second
for i in range(limit - 2):
    next = first + second
    if next > limit:
        break
    elif next % 2 == 0:
        sum += next
    first, second = second, next
print(sum)
