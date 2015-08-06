__author__ = 'Gabriel Fishman'
"""
POINT IN CIRCLE
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/98/
Having coordinates of the center of a circle, it's radius and coordinates of a point you need to define whether this
point is located inside of this circle.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

* Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)
* Center: (5.05, -11); Radius: 21.2; Point: (-31, -45)
* Center: (-9.86, 1.95); Radius: 47.28; Point: (6.03, -6.42)

All numbers in input are between -100 and 100

OUTPUT SAMPLE:

Print results in the following way.

* true
* false
* true
"""

import re
import sys

input_regex = re.compile("Center:\W\((?P<center_x>[-\d.]+),\W" +
                         "(?P<center_y>[-\d.]+)\);\W" +
                         "Radius:\W(?P<radius>[\d.]+);\W" +
                         "Point:\W\((?P<point_x>[-\d.]+),\W" +
                         "(?P<point_y>[-\d.]+)\)")

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        params = re.match(input_regex, test_case)
        center_x = float(params.group("center_x"))
        center_y = float(params.group("center_y"))
        radius = float(params.group("radius"))
        point_x = float(params.group("point_x"))
        point_y = float(params.group("point_y"))
        distance_squared = ((point_x - center_x) ** 2) + ((point_y - center_y) ** 2)
        print str(distance_squared <= radius ** 2).lower()


