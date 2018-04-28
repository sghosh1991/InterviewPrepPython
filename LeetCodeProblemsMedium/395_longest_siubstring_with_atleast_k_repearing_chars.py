'''

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

'''
import collections

class Solution(object):

    def __init__(self):
        self.calls = 0

    def longestSubstring(self, s, k, recLevel):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = collections.Counter(s)
        print "\n" + recLevel*"\t" + "Called with " + s + "  freq map " + str(freq)

        maxSubstrLenTillNow = -1
        idx = 0
        i = 0
        for i, ch in enumerate(s):
            print recLevel*"\t" + "Inside for loop i=" + str(i) + " ch=" + ch
            if(freq[ch] < k):
                print recLevel*"\t" + "Hit a non compliant character " + ch + " max substr length till now " + str(maxSubstrLenTillNow)
                # This char cant be in the answer
                self.calls += 1
                maxSubstrLenTillNow = max(maxSubstrLenTillNow, self.longestSubstring(s[idx:i], k, recLevel + 1))
                idx = i + 1

        print recLevel*"\t" + "Outside for loop idx=" + str(idx) + " i=" + str(i) + " maxsubstrtillnow=" + str(maxSubstrLenTillNow)
        if maxSubstrLenTillNow == -1:
            ans = len(s)
        else:
            self.calls += 1
            ans = max( maxSubstrLenTillNow, self.longestSubstring(s[idx:], k, recLevel+1))
        print recLevel*"\t" + "Returning maxSubStrLenTillNow =" + str(maxSubstrLenTillNow) + " idx =" + str(idx) + " ans=" + str(ans)
        return ans

if __name__ == "__main__":
    x = Solution()
    print "Ans = " + str(x.longestSubstring("abcde", 3, 0))
    #print "Ans = " + str(x.longestSubstring("aaabbb", 3, 0))
    #print "Ans = " + str(x.longestSubstring("ababacb", 3, 0))
    print " Recursive calls " + str(x.calls)