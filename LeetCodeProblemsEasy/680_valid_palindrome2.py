"""

"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right  = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left:right]) or self.isPalindrome(s[left+1: right+1])
            left += 1
            right -= 1
        return True


    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    x = Solution()
    print x.validPalindrome("abac")