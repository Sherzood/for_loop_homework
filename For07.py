def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    sum_odd_digit=0
    for i in range(N):
        if i%2!=0:
            sum_odd_digit+=i
    return sum_odd_digit
   