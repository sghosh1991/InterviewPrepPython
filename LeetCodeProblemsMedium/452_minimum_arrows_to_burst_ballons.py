"""
There are a number of spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal,
y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always
smaller than end. There will be at most 104 balloons.
An arrow can be shot up exactly vertically from different points along the x-axis.
A balloon with xstart and xend bursts by an arrow shot at x if xstart < x < xend.
There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely.
The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Idea sort by start time. LIne sweep left to right
When u hit an end point delete all the candidate baloons.
Idea is we fire off arrow at an end point

"""
from operator import itemgetter
class Solution(object):
    def endPointComparator(self, a, b):
        if a[0] != b[0]:
            return a[0] - b[0]
        else:
            # whoever is the start is lesser
            if a[1] == 'start':
                return -1
            else:
                return 1

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pointWithTypes = []
        burstBallonsCandidates = set() # Ballons that are supposed to get burst by the next arrow
        baloonBurstState = {}
        pointToInterval = {}
        for idx, point in enumerate(points):
            baloonBurstState[tuple(point)] = 0
            pointWithTypes.extend([(point[0], 'start', tuple(point)),(point[1], 'end', tuple(point))])
        #pointsSortedByStartTime = sorted(pointWithTypes, key=itemgetter(0))
        #print pointWithTypes
        pointsSortedByStartTime = sorted(pointWithTypes, cmp=self.endPointComparator)
        print pointsSortedByStartTime
        # for idx, point in enumerate(pointsSortedByStartTime):
        #     pointToInterval[(point[0], 'start', idx)] = tuple(point)
        #     pointToInterval[(point[1], 'end', idx)] = tuple(point)
        print pointToInterval
        #print baloonBurstState

        numArrowsNeeded = 0
        for idx, (point_x, point_type, point) in enumerate(pointsSortedByStartTime):
            print "Inspecting point " + str(point_x) + ":" + str(point_type)
            baloon = point
            print "Inspecting baloon " + str(baloon)
            if point_type == 'end':
                if not baloonBurstState[baloon]:
                    numArrowsNeeded += 1
                    for candidateBaloon in burstBallonsCandidates:
                        baloonBurstState[candidateBaloon] = 1
                    burstBallonsCandidates = set()
            else:
                # point type is start. This interval will get burtst by some arrow. So add it to the set of
                burstBallonsCandidates.add(baloon)
            print "Burst Baloons " + str(baloonBurstState)
            print "Candidate Baloons " + str(burstBallonsCandidates)
            print "Arrows needed " + str(numArrowsNeeded)
        return numArrowsNeeded

if __name__ == "__main__":
    x = Solution()
    #print x.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
    #print x.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
    print x.findMinArrowShots([[1,9],[7,16],[2,5],[7,12],[9,11],[2,10],[9,16],[3,9],[1,3]])

"""
BRILLIANT SOLUTION

class Solution(object):
    def findMinArrowShots(self, points):
        """
:type points: List[List[int]]
:rtype: int
"""
num = 0
right = -float('inf')
for interval in sorted(points):
    if interval[0] > right:
        num += 1
        right = interval[1]
    else:
        right = min(interval[1], right)
return num



"""
