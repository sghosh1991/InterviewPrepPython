"""

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

https://www.youtube.com/watch?v=J6o_Wz-UGvc

"""
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not len(nums):
            return []
        res = []
        dq = deque()
        #dq.appendleft(0)
        for i in range(len(nums)):
            print "\n" + "*"*20
            print "Inspecting element " + str(i) + ":" + str(nums[i])

            # Pop an element if the window size is 1 greater than k
            if len(dq) and (i - k) >= dq[0]:
                y = dq.popleft()
                print "Idx " + str(i) + " window size reached popping element with index" + str(y)

            while( len(dq) > 0 and nums[i] > nums[dq[-1]] ):
                x = dq.pop()
                print "Idx " + str(i) + "Incoming element is graeter than dq tail " + str(nums[x]) + " Removing " + str(x)

            dq.append(i)
            print "Current dequeue " + str(dq)
            if i >= k - 1:
                res.append(nums[dq[0]])
                print "Current result" + str(res)


        # The res only populates once it reaches >= k elements. If there are fewer elements than the window size the res may be empty.
        if len(res) == 0:
            res.append(nums[dq[0]])

        return res

if __name__ == "__main__":
    x = Solution()
    #print str(x.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    #print str(x.maxSlidingWindow([1,3,], 3))
    print str(x.maxSlidingWindow([1,-1], 1))
    print str(x.maxSlidingWindow([1,3,1,2,0,5], 3))

