'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''
from collections import deque
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        res = deque()
        carry = 0
        sum = 0

        len_num1 = len(num1)
        len_num2 = len(num2)

        num1_idx = num2_idx = -1

        while(num1_idx >= -len_num1 or num2_idx >= -len_num2):
            #print "in loop " + str(num1_idx) + " " + str(num2_idx)
            digit1 = int(num1[num1_idx]) if num1_idx >= -len_num1 else 0
            digit2 = int(num2[num2_idx]) if num2_idx >= -len_num2 else 0
            sum = carry + int(digit1) + int(digit2)
            carry = sum / 10
            #print " digit1 " + str(digit1)
            #print " digit1 " + str(digit2)
            res.appendleft(str(sum % 10))
            if(num1_idx >= -len_num1):
                num1_idx -= 1
            if(num2_idx >= -len_num2):
                num2_idx -= 1
        if(carry > 0):
            res.appendleft(str(carry))


        return "".join(res)

if __name__ == "__main__":
    x = Solution()
    print x.addStrings("99","9");