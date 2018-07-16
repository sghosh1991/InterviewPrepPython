"""

"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isAnsPositive = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            power = 1
            while (divisor << power) <= dividend:
                power += 1
            result += 1 << (power - 1)
            dividend -= (divisor << (power - 1))

        result = result if isAnsPositive else -result
        return result

if __name__ == "__main__":
    x = Solution()
    print x.divide(15, -4)


