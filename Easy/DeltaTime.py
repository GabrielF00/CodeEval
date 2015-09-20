import sys
from TimeStamp import TimeStamp

"""
DELTA TIME
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/166/

You are given the pairs of time values. The values are in the HH:MM:SS format with leading zeros.
Your task is to find out the time difference between the pairs.

INPUT SAMPLE:

The first argument is a file that contains lines with the time pairs.

For example:

* 14:01:57 12:47:11
* 13:09:42 22:16:15
* 08:08:06 08:38:28
* 23:35:07 02:49:59
* 14:31:45 14:46:56

OUTPUT SAMPLE:

Print to stdout the time difference for each pair, one per line. You must format the time values in HH:MM:SS with
leading zeros.

For example:

* 01:14:46
* 09:06:33
* 00:30:22
* 20:45:08
* 00:15:11
"""

__author__ = 'Gabriel Fishman'

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        time_one = TimeStamp(test.split(" ")[0])
        time_two = TimeStamp(test.strip().split(" ")[1])
        if time_one < time_two:
            print time_two - time_one
        else:
            print time_one - time_two
