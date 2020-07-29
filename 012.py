# https://projecteuler.net/problem=12

from math import sqrt, ceil

def divisors(number):
    i = 1
    divs = 0 
    while i <= sqrt(number):
        if number % i == 0:
            if number / i == i:
                divs += 1
            else:
                divs += 2
        i += 1 
    return divs

def triangular_numbers(divs=500):
    triangular = 0
    number = 1
    while True:
        triangular += number
        # Check for dividers
        div = divisors(triangular)
        if div > divs:
            return triangular 
        number += 1

if __name__ == "__main__":
    print(triangular_numbers())