def main(a):
    """
    If the number is positive, increase it to 1,otherwise decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    """
    if a > 0:
        a = a + 1

    if a < 0 :
        a = a - 2
    print(a)       
    return a
main(-5)