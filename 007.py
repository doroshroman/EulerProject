# https://projecteuler.net/problem=7

import math 

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_at(n):
    num = 2
    prime_number = num
    prime_count = 1 # because we have 2 already
    while prime_count != n:
        if is_prime(num) and num > 2:
            prime_number = num
            prime_count += 1
        num += 1
    return prime_number


if __name__ == "__main__":
    print(prime_numbers_at(10001))
        