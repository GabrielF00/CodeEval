import sys

__author__ = 'Gabriel Fishman'

"""
GAME OF LIFE
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/161/

The challenge is based on John Conway's 'Game of Life'. The Game of Life is a cellular automaton developed by the
British mathematician John Conway in 1970. The universe of the game is an infinite two-dimensional orthogonal grid of
square cells, each of which is in one of two possible states, alive or dead. Every cell that is horizontally,
vertically, or diagonally adjacent interacts with its eight neighbors. At each step in time, the following iterations
occur:

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overcrowding.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules
simultaneously to every cell in the seed - births and deaths occur simultaneously. The rules continue to be applied
repeatedly to create further generations.

You have a grid of size N x N, seeded with some live cells. Your task is to determine the state of the grid after 10
iterations.

INPUT SAMPLE:

The first argument is a file with the initial state of the grid. Alive cells are shown as asterisks '*', and dead cells
are shown as points '.'. E.g.

.........*
.*.*...*..
..........
..*.*....*
.*..*...*.
.........*
..........
.....*..*.
.*....*...
.....**...

OUTPUT SAMPLE:

Print to stdout the state of the grid after 10 iterations. E.g.

..........
...*......
..*.*.....
..*.*.....
...*......
..........
..........
..........
..........
..........

CONSTRAINTS:

The size of the grid in real input is 100 x 100 cells.
The cells outside the grid borders are assumed to be dead.
"""


def cell_value(x, y):
    if y < 0 or x < 0 or y > height - 1 or x > width - 1:
        return 0
    if grid[y][x] == "*":
        return 1
    else:
        return 0


def get_num_live_neighbors(x, y):

    count = 0
    # above and to the left
    count += cell_value(x - 1, y - 1)
    # above
    count += cell_value(x, y - 1)
    # above and to the right
    count += cell_value(x + 1, y - 1)
    # to the left
    count += cell_value(x - 1, y)
    # to the right
    count += cell_value(x + 1, y)
    # below and to the left
    count += cell_value(x - 1, y + 1)
    # below
    count += cell_value(x, y + 1)
    # below and to the right
    count += cell_value(x + 1, y + 1)
    return count

grid = []

with open(sys.argv[1], 'r') as lines:
    for line in lines:
        grid.append(list(line.strip()))

height = len(grid)
width = len(grid[0])

for iterations in range(10):

    neighbors = []
    for i in range(height):
        new = []
        for j in range(width):
            new.append(get_num_live_neighbors(j, i))
        neighbors.append(new)

    for i in range(height):
        for j in range(width):
            if grid[j][i] == "*":
                if neighbors[j][i] < 2:
                    grid[j][i] = "."
                elif neighbors[j][i] > 3:
                    grid[j][i] = "."
            elif grid[j][i] == ".":
                if neighbors[j][i] == 3:
                    grid[j][i] = "*"

for i in range(height):
    print str("".join(grid[i]))

