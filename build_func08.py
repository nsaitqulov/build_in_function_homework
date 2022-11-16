def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and return result:
    Args:
        x: int
        y: int
    Returns:
        result : int
    """
    a=5*pow(x, 2) * pow(y, 3) + x * pow(y, 2)
    return a

print(main(7, 1))