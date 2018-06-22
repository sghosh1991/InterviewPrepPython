"""
Tushar Roy you tube explanation
https://www.youtube.com/watch?v=nYFd7VHKyWQ&t=500s
"""
from collections import Counter
from copy import deepcopy

class Solution(object):


    def permutations(self, s):
        self.sLen = len(s)
        self.permuteHelper(["" for i in range(self.sLen)], 0, Counter(s), 0)

    def permuteHelper(self, partial_res, position, counter, stack):

        #print "\t"*stack + "Called with position " + str(position) + " " + str(counter)

        if self.sLen == position:
            print "\t"*stack + "Found a permutation " +  str(partial_res)
            return

        for ch in counter.keys():
            #print "\t"*stack + "Selecting character " + ch
            counter[ch] -= 1
            if counter[ch] == 0:
                del counter[ch]
            #print "\t"*stack + "Counter after selecting non zero character " + str(counter)
            partial_res[position] = ch
            self.permuteHelper(partial_res, position + 1, deepcopy(counter), stack + 1)
            # Restore the counter
            if ch not in counter:
                counter[ch] = 0
            counter[ch] += 1
            #print "\t"*stack + "Restored counter " + str(counter)


if __name__ == "__main__":
    x = Solution()
    x.permutations("aabc")
    x.permutations("abc")
