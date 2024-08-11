#!/usr/bin/python3
"""
Pascal's Triangle

--First Try--

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle =[]

    for row in range(n):
        ls = [1]
        if row == 0:
            triangle.append(ls)
        elif row == 1:
            ls.append(1)
            triangle.append(ls)
        else:
            for i in range(len(triangle[row-1]) - 1):
                new_elem = triangle[row-1][i] + triangle[row-1][i+1]
                ls.append(new_elem)
            ls.append(1)
            triangle.append(ls)
    return triangle
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
