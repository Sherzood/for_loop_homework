def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    sum_digit=0
    for i in range(A,B):
        sum_digit+=i
    return sum_digit
  