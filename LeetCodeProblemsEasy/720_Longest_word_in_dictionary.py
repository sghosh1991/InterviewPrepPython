'''

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographic


Solution:
Sort the list alphabetically
All prefixes are in order.
Iterate over the list


'''

class Solution(object):

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # sorted_words = sorted(words)
        # print "Sorted words \n" + str(sorted_words)
        # max_word_len = 0
        # i = self.firstSingleWord(0, sorted_words) + 1
        # num_words = len(sorted_words)
        # max_word = ""
        # while(i < num_words):
        #     print "Inspecting word at " + str(i) + " " + sorted_words[i]
        #     if(len(sorted_words[i-1]) != len(sorted_words[i]) - 1  or sorted_words[i-1][-1] != sorted_words[i][-2]):
        #         print "Cannot make " + sorted_words[i] + " from prefixes at " + str(i)
        #         i = self.firstSingleWord(i, sorted_words) + 1
        #         continue
        #     else:
        #         # This word can be built from its prefixes one word at a time from the begining
        #         valid_word_len = len(sorted_words[i])
        #         if(max_word_len < valid_word_len):
        #             max_word_len = valid_word_len
        #             max_word = sorted_words[i]
        #             print " max word at " +  str(i) + " " +  max_word
        #         i += 1
        #
        # return max_word

    # def firstSingleWord(self, i, words):
    #     words_len =  len(words)
    #     while(i < words_len):
    #         if len(words[i]) == 1:
    #             return i
    #         i += 1
    #     return i

if __name__ == "__main__":
    x = Solution()
    #print "Longest possible word length " + str(x.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
    print "Longest possible word " + str(x.longestWord(["rac","rs","ra","on","r","otif","o","onpdu","rsf","rs","ot","oti","racy","onpd"]))


