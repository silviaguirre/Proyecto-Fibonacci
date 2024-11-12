import sys
import argparse
from functools import lru_cache

def fibonacci_iterative(n:int)->int:
    """
        Computes the n-th Fibonacci number.
        :param n: n-th Fibonacci number.
        :return: The n-th Fibonacci number.
    """
    if n<0:
        raise ValueError("n must be greater tan or equal to zero.")
    if n < 2:
        return n
    else:
        a = 0
        b = 1
        for _ in range(n-1):
            a, b = b, a + b
        return b


@lru_cache(maxsize=100)
def fibonacci_recursive(n:int) -> int:
    """
    Computes the n-th Fibonacci number.
    :param n: n-th Fibonacci number.
    :return: The n-th Fibonacci number.
    """
    if n<0:
        raise ValueError("n must be greater tan or equal to zero.")
    if n < 2:
        return n
    else:
        return  fibonacci_recursive(n-1) + fibonacci_recursive(n-2)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('nth',type=int,help="Nth Fibonacci number.")
    args = parser.parse_args()
    result = fibonacci_iterative(args.nth)
    print(result)