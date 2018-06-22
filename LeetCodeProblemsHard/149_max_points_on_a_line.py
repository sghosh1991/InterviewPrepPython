"""

*** INCOMPLETE ****
Works in general. But getting TLE mostly because of the fraction class objects.
Will try to optimize in future. Logic is good.

A line is defined by slope and intercept.
slope = y2-y1/x2-x1
y_intercept = x2y1 - x1y2 / y2-y1

Incase of line s parallel to y axis
take slope = 1/0
x intercept = x/1as complete explanation

"""

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

from fractions import Fraction

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        line_by_points = {}
        max_points = 0
        for i, point_a in enumerate(points):
            for point_b in points[i+1:]:
                #print "Inspecting " + str(point_a) + " and " + str(point_b)
                # Lines parallel to y - axis:
                if point_a.x == point_b.x:
                    slope = (1, 0)
                    intercept = (point_a.x, 1)
                else:
                    slope = Fraction(point_b.y - point_a.y, point_b.x - point_a.x)
                    intercept = Fraction(point_b.x * point_a.y  - point_a.x * point_b.y, point_b.x - point_a.x)
                if (slope, intercept) not in line_by_points:
                    line_by_points[(slope, intercept)] = set()
                line_by_points[(slope, intercept)].add(point_a)
                line_by_points[(slope, intercept)].add(point_b)

        for line in line_by_points.keys():
            points_through_line = len(line_by_points[line])
            if points_through_line > max_points:
                max_points = points_through_line


        # print len(line_by_points.keys())
        # for line in line_by_points.keys():
        #     points_through_line = len(line_by_points[line])
        #     if points_through_line > max_points:
        #         max_points = points_through_line
        #     print str(line) + ":" + str(len(line_by_points[line]))
        #     for point in line_by_points[line]:
        #         print point
        # print max_points
        return max_points

if __name__ == "__main__":
    x = Solution()
    # points = [ [1,1], [2,2] ]
    # points = map(lambda x: Point(x[0], x[1]), points )
    # points = [[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],
    #           [5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],
    #           [0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],
    #           [-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],
    #           [-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],
    #           [-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],
    #           [-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],
    #           [-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],
    #           [2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],
    #           [-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],
    #           [-1,-15],[1,76],[-4,77],[6,-29]]
    points = [[1,1],[1,1],[2,2],[2,2]]
    points = map(lambda x: Point(x[0], x[1]), points )
    print x.maxPoints(points)




