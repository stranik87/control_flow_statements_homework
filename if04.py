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
    if a:
        a = (a+1)%2

    if b:
        b = (b+1)%2

    if c:
        c = (c+1)%2
    
    return a + b + c
print(main(1,2,4))
