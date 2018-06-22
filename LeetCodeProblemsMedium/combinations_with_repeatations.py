"""
https://www.youtube.com/watch?v=xTNFs5KRV_g&t=518s

"""

from collections import Counter
from copy import deepcopy

class Solution(object):


    def combinations(self, s):
        self.sLen = len(s)
        self.sArr = list(set(s))
        self.combinationHelper(["" for i in range(self.sLen)], 0, 0, Counter(s), 0)

    def findNextChar(self, pos, counter):
        for i in range(pos, len(self.sArr)):
            if self.sArr[i] in counter:
                return (i, self.sArr[i])
        return

    def combinationHelper(self, partial_res, position, pos_next_char, counter, stack):

        #print "\t"*stack + "Called with position " + str(position) + " pos next char " + str(pos_next_char) + " " + str(counter)

        print "\t"*stack + "Found a combination " +  str(partial_res[:position])
        for pos in range(pos_next_char, len(self.sArr)):
            x = self.findNextChar(pos, counter)
            if not x:
                return
            (pos_next_char, ch) = (x[0], x[1])
            #print "\t"*stack + "Selecting character " + ch + " at position " + str(pos_next_char)
            counter[ch] -= 1
            if counter[ch] == 0:
                del counter[ch]
            #print "\t"*stack + "Counter after selecting non zero character " + str(counter)
            partial_res[position] = ch
            self.combinationHelper(partial_res, position + 1, pos_next_char, deepcopy(counter), stack + 1)
            # Restore the counter
            # if ch not in counter:
            #     counter[ch] = 0
            # counter[ch] += 1
            # print "\t"*stack + "Restored counter " + str(counter)

if __name__ == "__main__":
    x = Solution()
    x.combinations("aabc")