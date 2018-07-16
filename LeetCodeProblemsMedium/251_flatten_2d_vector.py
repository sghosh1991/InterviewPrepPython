"""
https://leetcode.com/problems/flatten-2d-vector/description/
"""

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.row_counts = [len(x) for x in self.vec2d]
        self.curr_row = 0
        self.numRows = len(self.vec2d)

    def next(self):
        """
        :rtype: int
        """
        res = self.vec2d[self.curr_row][-self.row_counts[self.curr_row]]
        self.row_counts[self.curr_row] -= 1
        if self.row_counts[self.curr_row] == 0:
            self.curr_row += 1
        return res


    def hasNext(self):
        """
        :rtype: bool
        """
        while self.curr_row < self.numRows and self.row_counts[self.curr_row] == 0:
            self.curr_row += 1

        return self.curr_row < self.numRows


if __name__ == "__main__":
    matrix = [ [], [1,2], [], [4,5,6] ]
    matrix = [ [], [], [], [] ]
    i, v = Vector2D(matrix), []
    while i.hasNext():
        v.append(i.next())
    print v