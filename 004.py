# https://projecteuler.net/problem=4
import time

def is_palindrome(number):
    number = str(number)
    return number == number[::-1]

def biggest_palindrome():
    palindromes = []
    low_limit = 100
    high_limit = 1000
    for i in reversed(range(low_limit, high_limit)):
        for j in reversed(range(low_limit, high_limit)):
            prod = i * j
            if is_palindrome(prod):
                palindromes.append(prod)
    return max(palindromes)

if __name__ == '__main__':
    biggest_3_digit = biggest_palindrome()
    print(biggest_3_digit if biggest_3_digit else 'Not found')
                