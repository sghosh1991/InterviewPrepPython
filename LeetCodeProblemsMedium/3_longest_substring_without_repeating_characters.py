"""

Look at EPI pg: 323 for the solution hint

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenS = len(s)
        starting_idx = ans = 0
        element_idx_by_element = {}

        for idx, ch in enumerate(s):
            if ch not in element_idx_by_element:
                element_idx_by_element[ch] = idx
            else:
                earlier_idx_of_defaulting_elem = element_idx_by_element[ch]
                if earlier_idx_of_defaulting_elem >= starting_idx:
                    # This is an important case!!
                    # example abba. when looking at the last a we encounter a duplicate
                    # but we have already shifted the start idx to 2. So we are inspecting a
                    # new subarray begining at idx 2. Hence earlier idx of a  i.e 0 is invalid
                    ans = ans if ans > idx - starting_idx else idx - starting_idx
                    starting_idx = earlier_idx_of_defaulting_elem + 1
                element_idx_by_element[ch] = idx

        ans = ans if ans > lenS - starting_idx else lenS - starting_idx
        return ans

if __name__ == "__main__":
    x = Solution()
    # print x.lengthOfLongestSubstring("abcabcbb")
    # print x.lengthOfLongestSubstring("")
    # print x.lengthOfLongestSubstring("abc")
    # print x.lengthOfLongestSubstring("c")
    print x.lengthOfLongestSubstring("abba")