#!/usr/bin/python3
"""
function def island_perimeter(grid): that returns
the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """function definition"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:  # Check top neighbor
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left neighbor
                    perimeter -= 2

    return perimeter
