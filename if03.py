def main(a):
    """
    If the number is positive, increase it to 1,if the number is negative decrease it to 2.
    If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a > 0 :
        a = a + 1

    if a < 0 :
        a = a - 2    

    if a == 0 :
        a = 10   

    print(a)   
    return a
main(0)