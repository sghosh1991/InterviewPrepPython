'''

Write a function that takes a string as input and returns the string reversed.



'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # length = len(s)
        # s = list(s)
        # for i in range(length/2):
        #     temp_ch = s[i]
        #     s[i] = s[-(i+1)]
        #     s[-(i+1)] = temp_ch
        # return "".join(s)
        return s[::-1]