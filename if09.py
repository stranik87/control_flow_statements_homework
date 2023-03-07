def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    x1 = a%10
    x2 = a//10
    
    a2 = x1*10+x2

    if a2 <=a:
        print(True)

    if a2> a:
        print(False)    
    return a , a2

print(main(65))
