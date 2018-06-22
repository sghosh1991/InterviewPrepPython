"""
https://leetcode.com/problems/decode-ways/description/

Decode of 12 => Decode of 1 + decode of 2
                Decode of 12 + Decode of ""

Enumeration logic is different from counting logic.
Think of it like this. Lets say we have the string 12 and the dp array "somehow" has 1,2 which represents
that given the string 12 the number of decoings ending at index 1 which has 2 is dp[1] = 2. This is correct
as we can have AB or L
Now it becomes interesting. Lets add a 3rd digit say 3. Now how to think about this?
Adding 3 we can get  two ways:
1) Just consider 3 on its own as a single digit. Then the number of decode ways is what we already had for for the string ending at index 1 i.e '2'
So we have ABC LC --> 3 ==> C So C is taken on its own
2) take C and club it with the prev character 2. So now we have 23. This means we the number of ways is now what we had for index 0 i.e 1.
So we have AW
For every new character we consider we can do this take it on its own dp[n-1]
                               +
Club it with the prev character and get the number of ways for the string ebding two charecters away dp[n-2]
We have to deal with things like if after clubbing two charcters they are more bteween 26 and 10
We have to deal with 0 characters as well etc etc.
"""
from copy import copy
class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenS = len(s)
        if lenS == 0 or s[0] == '0':
            return 0
        dp = [0 for i in range(len(s))]
        dp[0] = 1

        if lenS >= 2:
            if int(s[:2]) <= 26:
                if s[1] != '0':
                    dp[1] = 2
                else:
                    dp[1] = 1
            else:
                if s[1] != '0':
                    dp[1] = 1
                else:
                    dp[1] = 0

            for i in range(2,len(s)):
                # Take the character on its own
                if s[i] != '0':
                    dp[i] += dp[i-1]
                # Couple this charecter with the prev one
                val = int(s[i-1:i+1])
                if val <= 26 and val >= 10:
                    dp[i] += dp[i-2]
        print dp
        return dp[-1]

    # def __init__(self):
    #     self.res = []

    # def numDecodings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     self.decode_helper("", s)
    #     return self.res
    #
    # def decode_helper(self, partial_res, s):
    #     print "Called with partial res " + str(partial_res) + " remaining " + s
    #
    #     if s[0] == '0':
    #         return
    #
    #     if s == "":
    #         self.res.append(partial_res)
    #         print "Hit empty remaining Result so far " + str(self.res)
    #     elif (len(s) == 1 and int(s) > 0):
    #         self.res.append(partial_res + chr(64 + int(s)))
    #         print "Hit single digit Result so far " + str(self.res)
    #     else:
    #         for i in range(2):
    #             digit = s[:i + 1]
    #             remaining = s[i+1:]
    #             if int(digit) <= 26 and int(digit) > 0:
    #                 partial_res_copy = copy(partial_res)
    #                 partial_res_copy += chr(64 + int(digit))
    #                 self.decode_helper(partial_res_copy, remaining)


if __name__ == "__main__":
    x = Solution()
    # x.numDecodings("123")
    # x.numDecodings("100")
    x.numDecodings("27")






