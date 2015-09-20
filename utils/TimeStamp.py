__author__ = 'Gabriel Fishman'


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

    def __sub__(self, other):
        if self.seconds < other.seconds:
            self.minutes -= 1
            self.seconds += 60
        self.seconds -= other.seconds

        if self.minutes < other.minutes:
            self.hours -= 1
            self.minutes += 60
        self.minutes -= other.minutes
        self.hours -= other.hours

        return self

    def __str__(self):
        return "{:0>2}:{:0>2}:{:0>2}".format(self.hours, self.minutes, self.seconds)
