# https://projecteuler.net/problem=14

def collatz_sequence(number):
    steps = 1
    while number != 1:
        # Odd number
        if number & 1:
            number = 3 * number + 1
        else:
            number //= 2
        steps += 1
    return steps

def longest_sequence(limit=1*10**6):
    max_steps = 0
    max_number = 1
    for n in range(1, limit):
        steps = collatz_sequence(n)
        if steps > max_steps:
            max_steps = steps
            max_number = n
    return max_number

if __name__ == "__main__":
    print(longest_sequence())