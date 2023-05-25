#!/usr/bin/python3

def island_perimeter(grid):
    """ Island perimeter
    Args:
        grid - lists of list of integers
    Return:
        perimeter of the island
    """
    if not grid or grid == []:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # One land cell add 4 to the perimeter
                perimeter += 4

                # check for adjacent cells to remove perimeter sides
                if i > 0 and grid[i - 1][j] == 1:
                    # remove 2 for each adjacent land cell in the same column
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    # remove 2 for each adjacent land cell in the same row
                    perimeter -= 2

    return perimeter
