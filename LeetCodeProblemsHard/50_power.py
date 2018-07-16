"""

"""
import time
class Solution(object):


    def myPow(self, x, n):
        self.cache = {}

        return self.myPowHelper(x,n)


    def myPowHelper(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        x = x if n > 0 else 1/float(x)
        n = abs(n)
        if n == 1:
            return x

        multiplier = 1 if n%2 == 0 else x
        if n/2 not in self.cache:
            self.cache[n/2] = self.myPowHelper(x, n/2)

        return multiplier * self.cache[n/2] * self.cache[n/2]

if __name__ == "__main__":
    x = Solution()
    stime = time.time()
    print "Result is : " + str(x.myPow(.1,2)) + " time taken: " + str(time.time()-stime)
    print "Result is : " + str(x.myPow(.00001,2147483647)) + " time taken: " + str(time.time()-stime)
