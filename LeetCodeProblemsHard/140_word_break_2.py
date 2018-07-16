"""

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        # DP solution
        T = [[] for i in range(len(s)+1)]
        T[0] = [""]
        wordDict = set(wordDict)
        #print T

        for prefix_length in range(1, len(s)+1):
            for j in range(0, prefix_length):
                if len(T[j]) > 0 and s[j:prefix_length] in wordDict:
                    for word in T[j]:
                        if word == "":
                            word += s[j:prefix_length]
                        else:
                            word = word + " " + s[j:prefix_length]
                        T[prefix_length].append(word)
        print T
        return T[len(s)]






    # TLE Solution
    # def wordBreak(self, s, wordDict):
    #     self.s = s
    #     self.wordDict = set(wordDict)
    #     res = self.wordBreakHelper(s, 0)
    #
    #     return [ " ".join(x) for x in res ]
    #
    #
    # def wordBreakHelper(self, s, stack):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: List[str]
    #     """
    #     print "\t"*stack + "Called with " + s
    #     res = []
    #     if s == "":
    #         return [[]]
    #
    #     for j in range(len(s)):
    #         prefix = s[:j+1]
    #         print "\t"*stack + "Extract substring 0" + "," + str(j) + " " + prefix
    #         if prefix in self.wordDict:
    #             print "\t"*stack + "Substr present in dict."
    #             partition_list = self.wordBreakHelper(s[j+1:], stack+1)
    #             print "\t"*stack + "Got back partition " + str(partition_list)
    #             for partition in partition_list:
    #                 partition.insert(0, prefix)
    #                 res.append(partition)
    #             print "\t"*stack + "Temporary result" + str(partition_list)
    #         else:
    #             print "\t"*stack + "Substr not in dict."
    #     print "\t"*stack + "Result " + str(res)
    #     return res

if __name__ == "__main__":
    x = Solution()
    x.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
    #x.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])