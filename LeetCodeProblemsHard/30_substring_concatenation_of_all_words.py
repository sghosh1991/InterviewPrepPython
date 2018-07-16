"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

Idea EPI Pg 325
Check each substring [i:nm -1] for the concatenation

"""
from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        lenWords = len(words)
        if lenWords == 0:
            return []
        self.word_unit_length = len(words[0])
        if self.word_unit_length == 0:
            return []
        self.num_words = len(words)
        res = []
        for i in range(0, len(s) - self.word_unit_length * self.num_words + 1):
            #print "Checking for substring " + str(i) + "," + str(i + self.word_unit_length * self.num_words)
            if self.isConcatenationOfAllWords(s[i : i + self.word_unit_length * self.num_words], words):
                print s[i:self.word_unit_length * self.num_words] + " contains all words from list "
                res.append(i)
        return res

    def isConcatenationOfAllWords(self, s, words):
        words_map = Counter(words)
        for i in range(0,self.word_unit_length*self.num_words , self.word_unit_length):
            substring_to_check = s[i:i+self.word_unit_length]
            if substring_to_check in words_map:
               if words_map[substring_to_check] == 1:
                   del words_map[substring_to_check]
               else:
                   words_map[substring_to_check] -= 1
            else:
                return False
        return len(words_map.keys()) == 0

if __name__ == "__main__":
    x = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print x.findSubstring(s, words)
    # s = "barfoothefoobarman"
    # words = ["bar"]
    # print x.findSubstring(s, words)
