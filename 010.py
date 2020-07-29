# https://projecteuler.net/problem=10

import math

def sum_prime_numbers(limit=2*10**6):
    # using eratosthenes sieve
    prime = [True] * limit
    for i in range(2, int(math.ceil(math.sqrt(limit)))):
        if prime[i]:
            j = i * i
            while j < limit:
                prime[j] = False
                j += i
    # -1 because of 1 is not prime number
    return sum(i for i, num in enumerate(prime) if num) - 1

if __name__ == "__main__":
    print(sum_prime_numbers())