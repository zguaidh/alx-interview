#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Pascal's Triangle
    """
    if n <= 0:
        return []
    else:
        nums = []
        for i in range(1, n + 1):
            C = 1
            ls = []
            for j in range(1, i+1):
                ls.append(C)
                C = C * (i - j) // j
            nums.append(ls)
        return nums
