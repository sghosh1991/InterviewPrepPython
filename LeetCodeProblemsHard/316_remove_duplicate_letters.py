"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
https://leetcode.com/problems/remove-duplicate-letters/description/
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        # TODO

if __name__ == "__main__":
    x = Solution()
    print x.removeDuplicateLetters("bcabc")
    print x.removeDuplicateLetters("cbacdcbc")