import argparse
import sys
from functools import cache


def fibonacci_iterative(n:int)->int:
    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")
    if n < 2:
        return n

    cont = 0
    n_1 = 1
    n_2 = 0
    sum = 0

    while(cont < n-1):
        sum = n_2 + n_1
        n_2 = n_1
        n_1 = sum
        cont+=1

    return sum

def fibonacci_recursive(n:int)->int:
    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")
    if n < 2:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive()

@cache
def fibonacci_recursive2(n:int)->int:
    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")
    if n < 2:
        return n
    nth = fibonacci_recursive2(n-1) + fibonacci_recursive2(n-2)
    return nth

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('nth',type=int, help= "Nth Fibonacci number")  # positional argument
    args = parser.parse_args()

    result = fibonacci_iterative(args.nth)
    print(result)
