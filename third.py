# https://projecteuler.net/problem=3

import math

number = 600851475143

def is_prime(num):
    sqrt = math.sqrt(num)
    start = 2
    while start <= sqrt:
        if num % start == 0:
            return False
        start += 1
    return True

start = 3 if sum(map(int, str(number).split())) else 2
for divider in range(start, number):
    if number % divider == 0 and is_prime(number // divider):
        print(number // divider)
        break
        