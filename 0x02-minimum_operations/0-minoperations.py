#!/usr/bin/python3

"""creates a function that takes n as an arguments and returns.

the number of operatiors required to print n characters
"""


def minOperations(n) -> int:
    """Return the minimum number of operations."""
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

