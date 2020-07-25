# https://projecteuler.net/problem=6

def square_sum(n=100):
    return sum(x**2 for x in range(1, n + 1))

def sum_square(n=100):
    return sum(x for x in range(1, n + 1))**2

if __name__ == '__main__':
    print(sum_square() - square_sum())