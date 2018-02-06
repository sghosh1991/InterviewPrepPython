"""

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place. The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Solution: U is cancelled by down right is cancelled by left

"""
import collections

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        frequency_count = collections.Counter(moves)
        return ( frequency_count['U'] == frequency_count['D'] ) and ( frequency_count['R'] == frequency_count['L'] )


if __name__ == '__main__':
    x = Solution()
    print x.judgeCircle("UD")