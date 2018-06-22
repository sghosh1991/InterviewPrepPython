"""

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""


"""

from heapq import heappush, heappop, heapify
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        res = []
        heap = []
        # sorted cahracter count array
        chrCount = sorted([(-S.count(ch), ch) for ch in set(S)])
        heapify(chrCount)
        print "Heap begining " + str(chrCount)
        while len(chrCount) >= 2:
            (chr1Count, chr1) = heappop(chrCount)
            (chr2Count, chr2) = heappop(chrCount)
            print "Added " + chr1 + " and " + chr2
            res.extend([chr1, chr2])
            chr1Count += 1
            chr2Count += 1
            if chr1Count:
                heappush(chrCount, (chr1Count, chr1))
            if chr2Count:
                heappush(chrCount, (chr2Count, chr2))
            print "Heap now " + str(chrCount)
        if len(chrCount):
            (count, chr) = heappop(chrCount)
            if -count > 1:
                res = []
            else:
                res.append(chr)
        return "".join(res)



if __name__ == "__main__":
    x = Solution()
    s = "vvvlo"
    print "Solution :" + x.reorganizeString(s)
    s = "qqqqq"
    print x.reorganizeString(s)

