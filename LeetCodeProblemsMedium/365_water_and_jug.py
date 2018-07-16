"""
https://leetcode.com/problems/water-and-jug-problem/description/


"""
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        jugs = (abs(x-y), x,y)
        self.cache = set()
        return self.canMeasureHelper(z, jugs)

    def canMeasureHelper(self, target, jugs):

        if target < 0 or target in self.cache:
            return False
        if target == 0:
            return True

        for water in jugs:
            if self.canMeasureHelper(target-water, jugs):
               return True

        self.cache.add(target)
        return False

if __name__ == "__main__":
    x = Solution()
    print x.canMeasureWater(3,5,4)
    print x.canMeasureWater(2,6,5)