"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

Same as base conversion here base is 26
And 1 = A...26 = Z
Because of this complexity the direct remainder wont work
We need to shift the remainder as per the fact that A = 1

So we cyclic left shift remainders
26 <- 0



"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        remainder = []
        while n:
            n -= 1
            remainder.append(n % 26)
            n /= 26


        result = [ chr(x + ord('A')) for x in reversed(remainder)]
        return "".join(result)

if __name__ == "__main__":
    x = Solution()
    print x.convertToTitle(28)
    #print x.convertToTitle(52)

