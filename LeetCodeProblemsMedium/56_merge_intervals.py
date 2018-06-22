"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

https://leetcode.com/problems/merge-intervals/description/

"""
from operator import attrgetter
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals = sorted(intervals, key=attrgetter('start'))
        print "Sorted intervals "
        self.print_intervals(intervals)
        res.append(intervals[0])
        for interval in intervals[1:]:
            print "Result till now"
            self.print_intervals(res)
            if self.overlaps(res[-1], interval):
                print "Overlap between " + str(res[-1]) + " and " + str(interval)
                res[-1] = self.merge_intervals(res[-1], interval)
            else:
                res.append(interval)
        print "Merging done...."
        self.print_intervals(res)

        return res

    def overlaps(self, i1, i2):
        return not (i2.start > i1.end) or (i1.start > i2.end)

    def merge_intervals(self, i1, i2):
        return Interval(min(i1.start, i2.start), max(i1.end, i2.end))

    def print_intervals(self, intervals):
        for i in intervals:
            print i

if __name__ == "__main__":
    x =Solution()
    intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    x.merge(intervals)
