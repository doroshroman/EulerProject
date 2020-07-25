# https://projecteuler.net/problem=5

def is_divisible(number, _range):
    for num in _range:
        if number % num != 0:
            return False
    return True

if __name__ == "__main__":
    start, end = 2, 20
    number = 2520
    while not is_divisible(number, [x for x in range(start, end)]):
        # we can update by 20
        number += 20
    else:
        print(number)
    