"""
https://leetcode.com/problems/partition-labels/description/

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        strLength = len(S)

        if not strLength:
            return res


        lastIdxByChr = {}
        for i,ch in enumerate(S):
            lastIdxByChr[ch] = i
        print lastIdxByChr
        print "*"*10

        start = 0
        farthestIdx = lastIdxByChr[S[start]]

        for i, ch in enumerate(S):
            if i == farthestIdx:
                res.append(i - start + 1)
                start = i+1
                if start < strLength:
                    farthestIdx = lastIdxByChr[S[start]]
                print "Partition found. Curr result " + str(res) + "\n"
            elif ch == S[farthestIdx]:
                pass
            elif lastIdxByChr[ch] > farthestIdx:
                farthestIdx = lastIdxByChr[ch]

            print "Farthest IDX " + str(farthestIdx) + ":" + S[farthestIdx]
            print "Start IDX " + str(start) + " End IDX " + str(i)
            print "Current Result " + str(S[start:i+1]) + "\n"

        return res

if __name__ == "__main__":
    x = Solution()
    s = "ababcbacadefegdehijhklij"
    print "Partition Lengths: " + str(x.partitionLabels(s))
    s = ""
    print "Partition Lengths: " + str(x.partitionLabels(s))

