"""
https://leetcode.com/problems/integer-to-roman/description/
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        neumerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = ""
        i = 0
        while(num > 0):
            if num - values[i] >= 0:
                num -= values[i]
                res += neumerals[i]
            else:
                i += 1
        print res
        return res

if __name__ == "__main__":
    x = Solution()
    x.intToRoman(59)
    x.intToRoman(7)
    x.intToRoman(204)
    x.intToRoman(72)