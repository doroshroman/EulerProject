# https://projecteuler.net/problem=9

def solve_pythagores_equation():
    ''' find a*b*c if a + b + c = 1000 
        where a^2 + b^2 = c^2

    '''
    x = y = z = 0
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            for c in range(b + 1, 1000):
                if a**2 + b**2 == c**2 and a + b + c == 1000: 
                    x, y, z = a, b, c
    return x * y * z
        
if __name__ == "__main__":
    print(solve_pythagores_equation())
