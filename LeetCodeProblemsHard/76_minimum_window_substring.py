"""
https://leetcode.com/problems/minimum-window-substring/description/
Have a solution if the target string does not contain duplicates.
My test cases are failing for target string with duplicates. Need to take a deeper look


"""
from collections import defaultdict, Counter
import sys

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        lenS = len(s)
        lenT = len(t)
        if not s or not t or lenS < lenT:
            return ""

        left = right = 0
        max_substr_length = sys.maxint
        max_substr_cover = ""
        target_char_length_by_char = defaultdict(int)

        unique_target_chars = set(t)
        self.target_char_map = Counter(t)


        while right < lenS :

            print "Entering expansion phase... left " + str(left) + " right " + str(right)
            #while right < lenS and len(target_char_length_by_char.keys()) < len(unique_target_chars):
            while right < lenS and not self.substring_found(target_char_length_by_char, self.target_char_map):
                if s[right] in unique_target_chars:
                    target_char_length_by_char[s[right]] += 1
                right += 1

            if len(target_char_length_by_char.keys()) == len(unique_target_chars):
                cover_length = right - left
                if cover_length < max_substr_length:
                    max_substr_length = cover_length
                    max_substr_cover = s[left:right]

            print "Entering contraction phase... left " + str(left) + " right " + str(right)
            # We have found a cover. Start chopping from right
            #while left < right and len(target_char_length_by_char.keys()) == len(unique_target_chars):
            while left < right and self.substring_found(target_char_length_by_char, self.target_char_map):
                print str(target_char_length_by_char)
                if s[left] in unique_target_chars:
                    if target_char_length_by_char[s[left]] == 1 :
                        print "Hit a substr cover at " + str(left) + "," + str(right) + " computing cover length"
                        cover_length = right - left
                        if cover_length < max_substr_length:
                            max_substr_length = cover_length
                            max_substr_cover = s[left:right]
                        del target_char_length_by_char[s[left]]
                    else:
                        print "Chopping of left element " + s[left] + " " + str(left) + " right " + str(right)
                        target_char_length_by_char[s[left]] -= 1
                left += 1
        return max_substr_cover

    def substring_found(self, d, src_dict):

        if len(d.keys()) == 0:
            return False

        for ch in src_dict.keys():
            if ch not in d or d[ch] < src_dict[ch]:
                return False
        return True


if __name__  == "__main__":
    x = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    # S = "aa"
    # T = "aa"
    S = "aaflslflsldkalskaaa"
    T ="aaa"
    print x.minWindow(S,T)




