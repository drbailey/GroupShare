__author__ = 'drew bailey'
""" Problem 1: Find the sum of all the multiples of 3 or 5 below 1000. """

def multiples(n):
    the_sum = 0
    for i in range(k):
        if i % 3 == 0 or i % 5 == 0:
            the_sum += i  # sum all results
    return the_sum

# only run if called from this script
if __name__ == '__main__':
    k = 1000
    print multiples(k)
