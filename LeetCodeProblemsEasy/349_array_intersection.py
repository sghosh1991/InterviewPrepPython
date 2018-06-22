"""

"""

class Solution(object):
    # def intersection(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """
    #     nums1Set = set(nums1)
    #     nums2Set = set(nums2)
    #     return list(nums2Set.intersection(nums1Set))

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not len(res) or nums1[i] != res[-1]:
                    res.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        print res
        return res

if __name__ == "__main__":
    x = Solution()
    x.intersection([1,2], [2,1])
    x.intersection([], [])
    x.intersection([1,2,2,1], [2,2])

