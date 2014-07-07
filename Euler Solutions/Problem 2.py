__author__ = 'drew bailey'
"""
Problem 2: By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""

def fib_less_than(n):
    a, b, c = 1, 2, 0
    the_sum = 2
    while c < n:
        c = a+b
        a, b = b, c
        if c % 2 == 0 and c < n:
            the_sum += c
    return the_sum

if __name__ == '__main__':
    k = 4000001
    print fib_less_than(n=k)
