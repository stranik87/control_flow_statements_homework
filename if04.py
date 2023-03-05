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
    x = (a+1)%2+(b+1)%2+(c+1)%2
    return x
print(main(1,2,4))
