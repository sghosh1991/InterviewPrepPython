'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].



I DONOT UNDERSTAND THE EXPLANATIONOR THE SOLUTION.
Y ARE WE COUNTING THE LAST STEP AS WELL?
[10, 15,20] MIN COST = 15 DOESNOT MAKE SENSE AT ALL
[0,0,1,1] = 0. BUT EXECTED IS 1 WTF??


'''
#  class Solution(object):

#     def __init__(self):
#         self.cache = {}

#     def minCostClimbingStairs(self, cost):
#         """
#         :type cost: List[int]
#         :rtype: int
#         """
#         return self.minCostClimbingStairsHelper(cost, len(cost)-1)


#     def minCostClimbingStairsHelper(self, cost, step):

#         print "Called for step " + str(step)
#         if(step in self.cache):
#             #print "Cache hit for step " + str(step)
#             return self.cache[step]
#         else:
#             #print "Cache miss for step " + str(step)
#             # Base case
#             if step == 0 or step == 1:
#                 return 0

#             minCost = min(cost[step-1] + self.minCostClimbingStairsHelper(cost, step-1),
#                        cost[step-2] + self.minCostClimbingStairsHelper(cost, step-2))
#             self.cache[step] = minCost
#             print "min cost at " + str(step) + " " + str(minCost)
#             return minCost