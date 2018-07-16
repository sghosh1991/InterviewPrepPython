"""

"""
import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(self.cleanseString(s))
        if len(s) == 0:
            return ""
        s = list(s)
        s = self.reverseString(s, 0, len(s)-1)
        left = i = 0
        while i < len(s):
            if s[i] == ' ':
                s[left:i] = self.reverseString(s, left, i-1)
                left = i + 1
            i += 1
        s[left:i] = self.reverseString(s, left, i-1)
        return "".join(s)

    def reverseString(self, s, left, right):

        l = left
        r = right
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s[l:r+1]

    def cleanseString(self, s):
        return re.sub( '\s+', ' ', s ).strip()



if __name__ == "__main__":
    x = Solution()
    #print x.reverseWords("ab cde fg")
    print x.reverseWords("   ab     cde fg   ")




