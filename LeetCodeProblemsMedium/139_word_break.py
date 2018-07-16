"""

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        T = [ False ]*(len(s)+1)
        T[0] = True

        # T[i] => if substring prefix ending at i can be partitioned into dictionary words
        # T[4] = True ==> s[0:5] can be partitioned into dictionary words. s[0:5] is exclusive if 5
        # We want to find T[len(s)]
        # Base condition => T0] = True
        # Recursive step => T[i] = if for any split at j between 0 and i
        # T[j] = True and s[j+1:i] is in dictionary, then s[0:i] can be split in
        # dictionary words
        for substring_length in range(1, len(s)+1):
            for j in range(0, substring_length):
                if T[j] and s[j:substring_length] in wordDict:
                    T[substring_length] = True
                    break
        print T
        return T[len(s)]

if __name__ == "__main__":
    x = Solution()
    print x.wordBreak("", ["apple", "pen"])
    #print x.wordBreak("applepenapple", ["apple", "pen"])