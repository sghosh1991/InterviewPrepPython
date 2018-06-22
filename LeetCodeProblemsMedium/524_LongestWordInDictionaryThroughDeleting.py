"""
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

Given a string and a string dictionary, find the longest string in the dictionary that can be
formed by deleting some characters of the given string. If there are more than one possible results,
return the longest word with the smallest lexicographical order. If there is no possible result,
return the empty string.



"""

import collections

class Solution(object):

    def __init__(self):
        self.srcString = ""

    def canBeCreatedFromSrcString(self,targetStr):
        revTargetStr = list(reversed(targetStr))
        for ch in self.srcString:
            if revTargetStr[-1] == ch:
                revTargetStr.pop()
                if len(revTargetStr) == 0:
                    return 1
        return 0


    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        self.srcString = s

        sortedDict = sorted(d, key=lambda x: (len(x), x))
        print "Sorted dict " + str(sortedDict)

        longestWordLength = 0
        longestWord = ""
        for word in sortedDict:
            if self.canBeCreatedFromSrcString(word) and len(word) > longestWordLength:
                longestWordLength = len(word)
                longestWord = word

        return longestWord

if __name__ == "__main__":
    x = Solution()
    s = "aewfafwafjlwajflwajflwafj"
    #d = ["ale","apple","monkey","plea","abc"]
    d = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]
    print x.findLongestWord(s,d)