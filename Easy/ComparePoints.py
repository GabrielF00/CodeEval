__author__ = 'Gabriel Fishman'
"""
COMPARE POINTS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/192/

Bob's hiking club is lost in the mountains on the way to a scenic overlook. Fortunately, Bob has a GPS device, so that
he can see the coordinates where the group is currently at. The GPS gives the current X/Y coordinates as O, P, and the
scenic overlook is located at Q, R. Bob now just needs to tell the group which way to go so they can get to the overlook
in time for s'mores.

INPUT SAMPLE:

The input is a file with each line representing a test case. Each test case consists of four integers O, P, Q, R on a
line, separated by spaces.


* 0 0 1 5
* 12 13 12 13
* 0 1 0 5

OUTPUT SAMPLE:

For each test case print a line containing one of the following: N, NE, E, SE, S, SW, W, NW, here if the coordinates
Q, R are (respectively) north, northeast, east, southeast, south, southwest, west, northwest, or already at ("here") the
coordinates O, P. Note that N, S, E and W mean directly North, South, East or West respectively, i.e. X or Y coordinates
of two points are exactly the same. In all other cases your output should be one of the NW, NE, SW, SE or here.

* NE
* here
* N
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        points = test_case.strip().split(" ")
        x1 = int(points[0])
        y1 = int(points[1])
        x2 = int(points[2])
        y2 = int(points[3])
        if y2 > y1:
            if x2 > x1:
                print "NE"
            elif x2 == x1:
                print "N"
            else:
                print "NW"
        elif y2 == y1:
            if x2 > x1:
                print "E"
            elif x2 == x1:
                print "here"
            else:
                print "W"
        else:
            if x2 > x1:
                print "SE"
            elif x2 == x1:
                print "S"
            else:
                print "SW"
