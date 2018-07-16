"""
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.total_length = 2*n
        self.generateParanthesisHelper("", n, n)
        return self.res

    def generateParanthesisHelper(self, partial_res, left_remaining, right_remaining):

        if len(partial_res) == self.total_length:
            self.res.append(partial_res)
            return

        if left_remaining:
            # Take the (
            self.generateParanthesisHelper( partial_res + '(', left_remaining - 1, right_remaining )

        if right_remaining > left_remaining:
            self.generateParanthesisHelper( partial_res + ')', left_remaining, right_remaining - 1 )

if __name__ == "__main__":
    x = Solution()
    x.generateParenthesis(3)