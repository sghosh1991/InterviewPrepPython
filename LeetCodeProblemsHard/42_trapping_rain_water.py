"""

https://leetcode.com/problems/trapping-rain-water/description/

Idea: For each bar find how much water can there be on top of the bar
Find the greatest height bar on the right side of each bar GR s.t it is greater than or equal to its own height
Find the greatest height bar on the left side of each bar GL s.t it is greater than or equal to its own height
Water on top of bar = min(GL,GR) - own height

"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) < 3:
            return 0

        # R to L scan to find GR
        max_bar_height_on_right = height[-1]
        max_on_right = []
        for bar_height in height[::-1]:
            max_bar_height_on_right = max(bar_height, max_bar_height_on_right)
            max_on_right.append(max_bar_height_on_right)

        max_on_right = max_on_right[::-1]
        #print max_on_right

        # L to R scan to find GR
        max_bar_height_on_left = height[0]
        max_on_left = []
        for bar_height in height:
            max_bar_height_on_left = max(bar_height, max_bar_height_on_left)
            max_on_left.append( max_bar_height_on_left )

        #print max_on_left

        total_water = 0
        for i in range(len(height)):
            s = min(max_on_right[i], max_on_left[i]) - height[i]
            total_water += s
            #print "Total water on top of bar " + str(height[i]) + "  is " + str(s)

        return total_water

if __name__ == "__main__":
    x = Solution()
    print x.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print x.trap([0,1,2,3,4,5])
    print x.trap([2,2,2,2])

