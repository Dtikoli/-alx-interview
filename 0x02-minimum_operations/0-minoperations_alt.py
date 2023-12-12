#!/usr/bin/python3
""" Calculates the fewest number of operations
needed to result in exactly n H characters in the file. """


def minOperations(n):
    """ Returns the fewest number of operations required to
    result in exactly n H characters in the file. """
    ops = 0
    for min_ops in range(2, int(n**0.5) + 1):
        while n % min_ops == 0:
            ops += min_ops
            n //= min_ops

    if n > 1:
        ops += n

    return ops
