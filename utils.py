from functools import reduce
from operator import mul
from math import ceil, sqrt

def seq_prod(sequence):
    return reduce(mul, sequence, 1)

def eratosthenes_sieve(N):
    primes = [True] * N
    for i in range(2, int(ceil(sqrt(N)))):
        if primes[i]:
            j = i * i
            while j < N:
                primes[j] = False
                j += i
    return primes
