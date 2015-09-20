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

import sys


class TimeStamp:
    def __init__(self, timestamp_str):
        self.str = timestamp_str
        timestamp_arr = timestamp_str.strip().split(":")
        self.hours = int(timestamp_arr[0])
        self.minutes = int(timestamp_arr[1])
        self.seconds = int(timestamp_arr[2])

    def compare_to(self, other):
        if self.hours > other.hours:
            return 1
        elif self.hours < other.hours:
            return -1

        if self.minutes > other.minutes:
            return 1
        elif self.minutes < other.minutes:
            return -1

        if self.seconds > other.seconds:
            return 1
        elif self.seconds < other.seconds:
            return -1

        return 0

    def __lt__(self, other):
        return self.compare_to(other) == -1

    def __eq__(self, other):
        return self.compare_to(other) == 0

    def __gt__(self, other):
        return self.compare_to(other) == 1

    def __str__(self):
        return self.str

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        timestamps = test.strip().split(" ")
        result = []
        for timestamp in timestamps:
            result.append(TimeStamp(timestamp))
        result.sort(reverse=True)
        print " ".join([str(item) for item in result])

