class Solution(object):
    def search(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        hi = len(arr)-1
        lo = 0
        while lo <= hi:
            mid = lo + (hi-lo)/2
            if target == arr[mid]:
                print "target " + str(target) + " found at " + str(mid)
                return mid
            print "Mid is " + str(mid)
            print "Inspecting array " + str(lo) + ":" + str(hi)
            # Right side is sorted
            if arr[mid] < arr[hi]:
                print "Right side of array is sorted"
                if arr[mid] <= target and target <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # Left half of array is sorted
            elif arr[lo] < arr[mid]:
                print "Left side of array is sorted"
                if arr[lo] <= target and target <= arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                lo = mid + 1
        return -1

if __name__ == "__main__":
    x = Solution()
    print x.search([4,5,6,7,1,2,3], 4)
