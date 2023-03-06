def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers

    """
    if a > 0:
        a = (a+1)%2

    if b > 0:
        b = (b+1)%2

    if c > 0:
        c = (c+1)%2
    
    return a + b + c
print(main(1,2,4))
