'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Solution Hint: http://wordaligned.org/articles/patience-sort
Patience Sorting


NOT DONE YET

'''
# import bisect
# class Solution(object):
#
#     def patienceSort(self, nums):
#         pileTops = []
#         piles = []
#         for num in nums:
#             pile = bisect.bisect_left(pileTops, num)
#             if(pile == len(pileTops)):
#                 piles.append([])
#                 piles[pile].append((num, len(piles[pile - 1]) - 1, None))
#                 (elem, prevTop, nextTop) = piles[pile-1][-1]
#                 nextTop =
#                 piles[pile-1][-1] = (elem, prevTop, nextTop)
#                 pileTops.append(num)
#             else:
#                 pileTops[pile] = num
#                 piles[pile].append((num, len(piles[pile - 1]) - 1, None))
#                 (elem, prevTop, nextTop) = piles[pile-1][len(piles[pile - 1])]
#                 nextTop = len(piles[pile])-1
#                 piles[pile-1][len(piles[pile - 1])] = (elem, prevTop, nextTop)
#
#         print piles
#         return piles
#
#     def findNumberOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         piles = self.patienceSort(nums)
#         routes = []
#         for i, pile in reversed(list(enumerate(piles))):
#             print " Inspecting pile " + str(pile) + " at pos " + str(i)
#             subRoutes = 0
#             for elem in pile:
#                 topOfPrevPile = elem[1]
#                 print "Prev pile top " + str(topOfPrevPile) + " pile " + str(list(reversed(piles[i-1][:topOfPrevPile+1])))
#                 for element in reversed(piles[i-1][ : topOfPrevPile+1]):
#                     print "Inspecting " + str(elem[0]) + " on pile " + str(i) + " with element " + str(element[0]) + " on pile " + str(i-1)
#                     if elem[0] > element[0]:
#                         subRoutes += 1
#                         print "sub routes added " + str(subRoutes)
#             routes.append(subRoutes)
#
#
#
#
# # # We want a maximum function which accepts a default value
# # from functools import partial, reduce
# # maximum = partial(reduce, max)
# #
# # def patience_sort(xs):
# #     '''Patience sort an iterable, xs.
# #
# #     This function generates a series of pairs (x, pile), where "pile"
# #     is the 0-based index of the pile "x" should be placed on top of.
# #     Elements of "xs" must be less-than comparable.
# #     '''
# #     pile_tops = list()
# #     for x in xs:
# #         pile = bisect.bisect_left(pile_tops, x)
# #         if pile == len(pile_tops):
# #             pile_tops.append(x)
# #         else:
# #             pile_tops[pile] = x
# #         yield x, pile
# #
# #     # print pile_tops
# #     # return pile_tops
# # def longest_increasing_subseq_length(xs):
# #     return 1 + maximum((pile for x, pile in patience_sort(xs)), -1)
# #
# # def longest_increasing_subsequence(xs):
# #     # Patience sort xs, stacking (x, prev_ix) pairs on the piles.
# #     # Prev_ix indexes the element at the top of the previous pile,
# #     # which has a lower x value than the current x value.
# #     piles = [[]] # Create a dummy pile 0
# #     for x, p in patience_sort(xs):
# #         if p + 1 == len(piles):
# #             piles.append([])
# #         # backlink to the top of the previous pile
# #         piles[p + 1].append((x, len(piles[p]) - 1))
# #         # Backtrack to find a longest increasing subsequence
# #     print piles
# #     npiles = len(piles) - 1
# #     prev = 0
# #     lis = list()
# #     for pile in range(npiles, 0, -1):
# #         x, prev = piles[pile][prev]
# #         lis.append(x)
# #     lis.reverse()
# #     return lis
#
#
#
# if __name__ == "__main__":
#     x = Solution()
#     print x.findNumberOfLIS([1,2,4,3,5, 2.5, 4,7,2])
#
#     #print longest_increasing_subsequence([-1,2,4,3,5,4,7,1])

class Solution(object):
    def findNumberOfLIS(self):
        pass



if __name__ == "__main__":
    x = Solution()
    print x.findNumberOfLIS([1,2,5,3,7,6])