def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a > 0:
        a = 0

    if a < 0:
        a = 1

    if b > 0:
        b = 0

    if b < 0:
        b = 1

    if c > 0:
        c = 0
    if c < 0:
        c = 1                   
    return a + b + c

print(main(-5,6,-7))

