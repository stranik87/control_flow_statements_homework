def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if (a%2 == 1) > 0:
        print("положительное нечетное число")

    if (a%2 == 0)> 0:
        print("положительное четное число")

    if (a%2 == 1) < 0:
        print( "отрицательное нечетное число")
    if (a%2 == 0) < 0:
        print("отрицательное четное число")    

    if a == 0:
        print( "число равно нулю")    
    return a


print(main(0))