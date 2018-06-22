"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

https://leetcode.com/problems/non-overlapping-intervals/description/


Logic: Activity selection problem gives maximum number fo no - overlapping intervals
Complement the result to get the minimum number of intervals to remove
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"

from operator import itemgetter, attrgetter

class Solution(object):

    def eraseOverlapIntervals(self, intervals):

        self.printIntervals(intervals)
        print "#"*10
        # Add all intervals to a set
        allIntervals = set(intervals)

        # sort intervaks by finish time
        intervalsSortedFinishTime = sorted(intervals, key=attrgetter('end'))
        self.printIntervals(intervalsSortedFinishTime)
        print "#"*10

        maxNonOverlappingIntervals = [intervalsSortedFinishTime[0]]
        allIntervals.remove(intervalsSortedFinishTime[0])

        for interval in intervalsSortedFinishTime[1:]:
            lastAddedInterval = maxNonOverlappingIntervals[-1]
            if interval.start >= lastAddedInterval.end:
                print "Added interval " + str(interval)
                maxNonOverlappingIntervals.append(interval)
                allIntervals.remove(interval)

        self.printIntervals(maxNonOverlappingIntervals)
        return len(allIntervals)

    def printIntervals(self, intervals):
        for i in intervals:
            print i

if __name__ == "__main__":
    x = Solution()
    intervals = [ Interval(1,2), Interval(2,3), Interval(3,4), Interval(1,3) ]
    print "Minumum nunber of intervals to remove " + str(x.findMaximunNonOverLappingIntervals(intervals))
    intervals = [ Interval(1,2), Interval(1,2), Interval(1,2) ]
    print "Minumum nunber of intervals to remove " + str(x.findMaximunNonOverLappingIntervals(intervals))


