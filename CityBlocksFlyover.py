__author__ = 'Gabriel Fishman'

import sys

'''
Problem Description:

See https://www.codeeval.com/open_challenges/133/
In our city we need to know how many blocks were impacted by a helicopter flying over our city.
In our city, all of the blocks are rectangular. They are separated by N number of straight horizontal avenues that run
East-West and M number of straight vertical streets which run North-South.

A helicopter took off at the South-West corner of the city and flew directly to the farthest North-East corner.
Your challenge is to determine how many city blocks it flew over?
You will be given two lists, the first one is for streets and the second one is for avenues.
Each avenue and each street is represented by a distance D to itself from the helicopter's starting point. E.g.

On the first diagram the streets and the avenues are represented by the following lists:

(0,1,3,4,6) for streets
(0,1,2,4) for avenues
The blocks the helicopter has flown over are colored dark grey.
The inner region of each small rectangle is a city block. Rectangles' borders are not considered as a part of a block.

'''

def evaluateCell(xvals, yvals, cell_x1_idx, cell_y1_idx, line_m, cellCount):
    """
    Calculate cell_intercept: the y-value of the helicopter's path when it intersects x = the right side of the current
    cell. cell_y1 is y-value of the top-right corner of the current cell.
    If cell_intercept is equal to the top-right corner of the current cell, then the helicopter passes directly through
    the top-right corner of the cell. Examine the cell whose bottom-left corner is the current cell's top-right corner.
    If cell_intercept < cell_y1, the helicopter exits on the right side of the cell, so we examine the cell to the
    right of the current cell.
    If cell_intercept > cell_y1, the helicopter exits on the top of the current cell, so we examine the cell on top
    of the current cell.

    :param xvals: the list of streets
    :param yvals: the list of avenues
    :param cell_x1_idx: the x coordinate of the top right corner of the current box
    :param cell_y1_idx: the y coordinate of the top right corner of the current box
    :param line_m: the slope of the line between southwest and northeast corners of the city
    :param cellCount: the number of cells examined
    :return: the number of cells which the helicopter passes over
    """
    cell_x1 = xvals[cell_x1_idx]
    cell_y1 = yvals[cell_y1_idx]
    cell_intercept = line_m * cell_x1

    if cell_x1_idx == len(xvals) - 1 and cell_y1_idx == len(yvals) - 1:
        return cellCount

    if cell_intercept == float(cell_y1):
        return evaluateCell(xvals, yvals, cell_x1_idx + 1, cell_y1_idx + 1, line_m, cellCount + 1)
    elif cell_intercept < float(cell_y1):
        return evaluateCell(xvals, yvals, cell_x1_idx + 1, cell_y1_idx, line_m, cellCount + 1)
    elif cell_intercept > float(cell_y1):
        return evaluateCell(xvals, yvals, cell_x1_idx, cell_y1_idx + 1, line_m, cellCount + 1)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.replace("(", "")
    test = test.replace(")", "")

    test_split = test.split(" ", 2)
    xval_string = test_split[0]
    yval_string = test_split[1]

    xvals = [int(s) for s in xval_string.split(',')]
    yvals = [int(s) for s in yval_string.split(',')]

    line_slope = float(yvals[len(yvals) - 1]) / xvals[len(xvals) - 1]

    print evaluateCell(xvals, yvals, 1, 1, line_slope, 1)

test_cases.close()