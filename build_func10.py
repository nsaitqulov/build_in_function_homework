def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and round the result to 2 decimal places, use the pow function use the round function ,return result:
    Args:
        x: int
        y: int
    Returns:
        result : float
    """
    a=3*pow(y, 1/2) + pow(x, 2/3)
    return a
print(main(8, 4))
