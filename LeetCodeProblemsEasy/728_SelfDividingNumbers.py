"""

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.


"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [x for x in range(left, right+1) if self.isSelfDividing(x)]

    def isSelfDividing(self, num):
        digits = []
        orig_num = num
        while num:
            digit = num % 10
            if digit == 0 or orig_num % digit != 0:
                return False
            else:
                digits.append(digit)
                num /= 10
        return True

if __name__ == "__main__":
    x = Solution()
    print x.selfDividingNumbers(1,22)