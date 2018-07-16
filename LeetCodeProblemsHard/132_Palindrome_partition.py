"""

Tushar roy's solution gives TLE in Leetcode. Even if i use a cache to
compute the isPalindrome.
EPI solution is much mmore elegant. Takes a lot less time
as it does not consider for various length substrings. It deals with suffixes

"""
import time

class Solution(object):

    def isPalindrome(self, i, j):

        if self.s[i] != self.s[j]:
            self.palindromeCache[i][j] = False
        else:
            if j - i == 1:
                self.palindromeCache[i][j] = True
            else:
                self.palindromeCache[i][j] = self.palindromeCache[i+1][j-1]

        #print self.s[i:j+1] + " is a palindrome " + str(self.palindromeCache[i][j])
        return self.palindromeCache[i][j]

        # lo = i
        # hi = j
        # while lo < hi:
        #     if self.s[lo] != self.s[hi]:
        #         return False
        #     lo += 1
        #     hi -= 1
        # return True

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenS = len(s)
        if lenS == 0:
            return 0
        T = [ [0]*lenS for i in range(lenS) ]
        self.s = s
        self.palindromeCache = [ [False]*len(s) for i in range(len(s)) ]
        for i in range(lenS):
            self.palindromeCache[i][i] = True

        for substringLength in range(2, lenS + 1):
            for i in range(0, lenS-substringLength + 1):
                j = i + substringLength - 1
                #print "Inspecting " + str(i) + "," + str(j) + " : " + s[i:j+1]
                if not self.isPalindrome(i, j):
                    palindromePartitionLengths = []
                    for k in range(i, j):
                        palindromePartitionLengths.append(1+T[i][k]+T[k+1][j])
                        T[i][j] = min(palindromePartitionLengths)


        self.printMatrix(T)
        return T[0][lenS-1]

    def minCut2(self, s):

        palindrome = [ [False]*len(s) for i in range(len(s))]
        T = [i for i in range(-1, len(s))]
        T = T[::-1]
        #print T

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or palindrome[i+1][j-1]):
                    palindrome[i][j] = True
                    T[i] = min(T[i], 1 + T[j+1])

        #self.printMatrix(palindrome)
        #print T
        return T[0]

    def printMatrix(self, T):
        print "*"*30
        for i in range(len(T)):
            print T[i]


if __name__ == "__main__":
    x = Solution()
    # print x.minCut("abcbm")
    # print x.minCut("aba")
    # print x.minCut("ab")
    # print x.minCut("a")
    stime = time.time()
    #print x.minCut2("aab")
    print x.minCut2("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
    print "Took " + str(time.time() - stime ) + " seconds"