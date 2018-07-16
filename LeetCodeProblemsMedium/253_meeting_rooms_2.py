"""

"""
import heapq
from operator import attrgetter

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "( " + str(self.start) + "," + str(self.end) + " )"

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals_sorted_stime = sorted(intervals, key=attrgetter('start'))
        self.printIntervals(intervals_sorted_stime)

        meeting_rooms = []
        heapq.heappush(meeting_rooms, ( intervals_sorted_stime[0].end,  intervals_sorted_stime[0] ))
        min_meeting_rooms_needed = 1
        self.printHeap(meeting_rooms)
        for interval in intervals_sorted_stime[1:]:
            print "Considering interval " + str(interval)
            if self.isIntervalCompatible(interval, meeting_rooms[0][1]):
                print "Interval compatible with the minimum end time interval. Taking the meeting room where meeting has ended"
                heapq.heapreplace(meeting_rooms, ( interval.end, interval ))
            else:
                # Allocate a new meeting room
                print "interval not compatible with the minimmum end time interval. Allocating new meeting room"
                heapq.heappush(meeting_rooms, (interval.end, interval))

            min_meeting_rooms_needed = max(min_meeting_rooms_needed, len(meeting_rooms))
            self.printHeap(meeting_rooms)
            print "Num meeting rooms :" + str(min_meeting_rooms_needed)

        return min_meeting_rooms_needed

    def printIntervals(self, intervals):
        for x in intervals:
            print x

    def printHeap(self, intervals):
        for x in intervals:
            print str(x[0]) + " " + str(x[1])



    def isIntervalCompatible(self, i1, i2):
        return i2.start >= i1.end or i1.start >= i2.end


if __name__ == "__main__":
    x = Solution()
    #intervals = [[0, 30],[5, 10],[15, 20]]
    intervals = [[7,10],[2,4]]
    interval_objects = map( lambda x: Interval(x[0], x[1]), intervals)
    x.minMeetingRooms(interval_objects)





