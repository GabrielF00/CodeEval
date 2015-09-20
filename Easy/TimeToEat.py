import sys
from TimeStamp import TimeStamp

__author__ = 'Gabriel Fishman'
"""
TIME TO EAT
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/214/

INPUT SAMPLE:

The first argument is a path to a file. Each line includes a test case: a schedule containing unsorted timestamps
in HH:MM:SS format.

For example:

* 02:26:31 14:44:45 09:53:27
* 05:33:44 21:25:41

OUTPUT SAMPLE:

Sort timestamps in each schedule from the biggest to the smallest one.

* 14:44:45 09:53:27 02:26:31
* 21:25:41 05:33:44

"""

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        timestamps = test.strip().split(" ")
        result = []
        for timestamp in timestamps:
            result.append(TimeStamp(timestamp))
        result.sort(reverse=True)
        print " ".join([str(item) for item in result])

